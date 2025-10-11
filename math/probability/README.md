# Probability Tutorial

This is a comprehensive **Probability Tutorial** covering fundamental concepts, discrete and continuous distributions, and their key formulas.

---

## 1. Introduction to Probability

**Probability** measures the likelihood of an event occurring. It ranges from 0 (impossible) to 1 (certain).  

For a sample space \( S \) and event \( A \subseteq S \):

\[
P(A) = \frac{\text{Number of outcomes in } A}{\text{Total number of outcomes in } S}
\]

**Complement Rule:**

\[
P(A^c) = 1 - P(A)
\]

**Addition Rule:**

\[
P(A \cup B) = P(A) + P(B) - P(A \cap B)
\]

**Multiplication Rule (independent events):**

\[
P(A \cap B) = P(A) \cdot P(B)
\]

---

## 2. Random Variables

A **random variable** assigns a numerical value to each outcome in a sample space.

- **Discrete:** Countable values (e.g., number of heads in coin tosses)  
- **Continuous:** Any value in a range (e.g., time, height)

---

## 3. Expected Value and Variance

For a discrete random variable \( X \) with values \( x_i \) and probabilities \( P(X=x_i) \):

\[
E[X] = \sum_i x_i P(X=x_i)
\]

\[
\text{Var}(X) = \sum_i (x_i - E[X])^2 P(X=x_i)
\]

For continuous random variables with PDF \( f(x) \):

\[
E[X] = \int_{-\infty}^{\infty} x f(x) \, dx, \quad
\text{Var}(X) = \int_{-\infty}^{\infty} (x - E[X])^2 f(x) \, dx
\]

---

## 4. Discrete Probability Distributions

### 4.1 Poisson Distribution

- **Use:** Number of events in a fixed interval  
- **Parameter:** \( \lambda \) = expected occurrences  

**PMF:**

\[
P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!}, \quad k = 0,1,2,\dots
\]

**CDF:**

\[
F(k) = P(X \le k) = \sum_{i=0}^{k} \frac{\lambda^i e^{-\lambda}}{i!}
\]

**Mean and Variance:**

\[
E[X] = \lambda, \quad \text{Var}(X) = \lambda
\]

---

### 4.2 Binomial Distribution

- **Use:** Number of successes in \( n \) independent trials  
- **Parameters:** \( n \) = trials, \( p \) = success probability  

**PMF:**

\[
P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}, \quad k = 0,1,2,\dots,n
\]

**CDF:**

\[
F(k) = P(X \le k) = \sum_{i=0}^{k} \binom{n}{i} p^i (1-p)^{n-i}
\]

**Mean and Variance:**

\[
E[X] = n p, \quad \text{Var}(X) = n p (1-p)
\]

---

## 5. Continuous Probability Distributions

### 5.1 Exponential Distribution

- **Use:** Time between events in a Poisson process  
- **Parameter:** \( \lambda \) = rate of occurrence  

**PDF:**

\[
f(x) = \lambda e^{-\lambda x}, \quad x \ge 0
\]

**CDF:**

\[
F(x) = P(X \le x) = 1 - e^{-\lambda x}, \quad x \ge 0
\]

**Mean and Variance:**

\[
E[X] = \frac{1}{\lambda}, \quad \text{Var}(X) = \frac{1}{\lambda^2}
\]

---

### 5.2 Normal (Gaussian) Distribution

- **Use:** Continuous symmetric data around a mean  
- **Parameters:** \( \mu \) = mean, \( \sigma \) = standard deviation  

**PDF:**

\[
f(x) = \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{(x - \mu)^2}{2 \sigma^2}}
\]

**CDF:**

\[
F(x) = P(X \le x) = \frac{1}{2} \left[ 1 + \operatorname{erf} \left( \frac{x - \mu}{\sigma \sqrt{2}} \right) \right]
\]

**Z-score:**

\[
z = \frac{x - \mu}{\sigma}
\]

**X-value from Z-score:**

\[
x = z \cdot \sigma + \mu
\]

**Mean and Variance:**

\[
E[X] = \mu, \quad \text{Var}(X) = \sigma^2
\]

---

## 6. Relationships Between Distributions

- **Poisson approximates Binomial** for large \( n \) and small \( p \)  
- **Exponential is the continuous analog of Poisson** (time between events)  
- **Normal approximates Binomial and Poisson** under the Central Limit Theorem

---

## 7. Summary Table

| Distribution | Type       | Parameters      | Mean           | Variance        | Notes |
|-------------|-----------|----------------|---------------|----------------|------|
| Poisson     | Discrete  | λ              | λ             | λ              | Count events |
| Binomial    | Discrete  | n, p           | n·p           | n·p(1-p)       | Count successes in trials |
| Exponential | Continuous| λ              | 1/λ           | 1/λ²           | Time between events |
| Normal      | Continuous| μ, σ           | μ             | σ²             | Bell curve, symmetric |

---

This tutorial provides a complete reference for **probability theory, key distributions, and formulas** for educational purposes.
