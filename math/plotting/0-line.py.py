#!/usr/bin/env python3
"""
Complete the following source code to plot y as a line graph:

y should be plotted as a solid red line
The x-axis should range from 0 to 10
"""
import numpy as np
import matplotlib.pyplot as plt

y = np.arange(0, 11) ** 3

# your code here
x = np.arange(0, 10)
# plot a line graph
plt.plot(y, color='red', linestyle='solid')
plt.show()
