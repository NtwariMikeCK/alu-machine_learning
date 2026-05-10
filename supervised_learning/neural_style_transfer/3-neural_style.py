#!/usr/bin/env python3
"""
3-neural_style.py
"""

import tensorflow as tf
import numpy as np


class NST:
    """
    Neural Style Transfer class
    """

    style_layers = ['block1_conv1',
                    'block2_conv1',
                    'block3_conv1',
                    'block4_conv1',
                    'block5_conv1']

    content_layer = 'block5_conv2'

    def __init__(self, style_image, content_image,
                 alpha=1e4, beta=1):
        """
        Class constructor
        """

        if (not isinstance(style_image, np.ndarray) or
                len(style_image.shape) != 3 or
                style_image.shape[2] != 3):
            raise TypeError(
                "style_image must be a numpy.ndarray "
                "with shape (h, w, 3)"
            )

        if (not isinstance(content_image, np.ndarray) or
                len(content_image.shape) != 3 or
                content_image.shape[2] != 3):
            raise TypeError(
                "content_image must be a numpy.ndarray "
                "with shape (h, w, 3)"
            )

        if (not isinstance(alpha, (int, float)) or alpha < 0):
            raise TypeError(
                "alpha must be a non-negative number"
            )

        if (not isinstance(beta, (int, float)) or beta < 0):
            raise TypeError(
                "beta must be a non-negative number"
            )

        tf.config.run_functions_eagerly(True)

        self.style_image = self.scale_image(style_image)
        self.content_image = self.scale_image(content_image)

        self.alpha = alpha
        self.beta = beta

        self.load_model()
        self.generate_features()

    @staticmethod
    def scale_image(image):
        """
        Rescale image
        """

        if (not isinstance(image, np.ndarray) or
                len(image.shape) != 3 or
                image.shape[2] != 3):
            raise TypeError(
                "image must be a numpy.ndarray "
                "with shape (h, w, 3)"
            )

        h, w, _ = image.shape

        if h > w:
            new_h = 512
            new_w = int(w * 512 / h)
        else:
            new_w = 512
            new_h = int(h * 512 / w)

        image = tf.convert_to_tensor(image, dtype=tf.float32)
        image = tf.image.resize(
            image,
            (new_h, new_w),
            method=tf.image.ResizeMethod.BICUBIC
        )

        image = image / 255.0
        image = tf.clip_by_value(image, 0, 1)
        image = tf.expand_dims(image, axis=0)

        return image

    def load_model(self):
        """
        Load VGG19 model for feature extraction
        """

        vgg = tf.keras.applications.VGG19(
            include_top=False,
            weights='imagenet'
        )
        vgg.trainable = False

        outputs = [vgg.get_layer(name).output
                   for name in self.style_layers]
        outputs.append(vgg.get_layer(self.content_layer).output)

        self.model = tf.keras.Model(inputs=vgg.input, outputs=outputs)

    @staticmethod
    def gram_matrix(input_layer):
        """
        Calculates gram matrix
        """

        if (not tf.is_tensor(input_layer) or
                len(input_layer.shape) != 4):
            raise TypeError(
                "input_layer must be a tensor of rank 4"
            )

        # shape: (1, h, w, c)
        result = tf.linalg.einsum(
            'bhwc,bhwd->bcd',
            input_layer,
            input_layer
        )

        h = tf.cast(tf.shape(input_layer)[1], tf.float32)
        w = tf.cast(tf.shape(input_layer)[2], tf.float32)

        return result / (h * w)

    def generate_features(self):
        """
        Extract style and content features
        """

        style_outputs = self.model(self.style_image)
        content_outputs = self.model(self.content_image)

        # style features → gram matrices
        self.gram_style_features = [
            self.gram_matrix(style_outputs[i])
            for i in range(len(self.style_layers))
        ]

        # content feature → last output
        self.content_feature = content_outputs[-1]
