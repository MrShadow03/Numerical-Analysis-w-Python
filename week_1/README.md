# 🧮 Numerical Analysis with Python

## 📘 Introduction to Numerical Analysis

Numerical Analysis is a branch of mathematics that focuses on developing and analyzing numerical algorithms to solve real-world mathematical problems. Unlike symbolic computation (where exact solutions are found), numerical analysis focuses on **approximate solutions** with a high degree of accuracy.

### 🔍 Why is Numerical Analysis Important?

- Many mathematical problems cannot be solved analytically.
- Real-world data is often messy and complex.
- Useful in engineering, physics, computer science, finance, machine learning, and more.
- Efficient numerical methods allow for solving large-scale, complex problems using computers.

### 🛠 Common Topics in Numerical Analysis

- Error Analysis (round-off, truncation)
- Root-Finding Methods
- Numerical Linear Algebra
- Interpolation & Curve Fitting
- Numerical Integration & Differentiation
- Solving Differential Equations

---

## 📐 Babylonian Method for Finding Square Roots

### 🏺 Historical Background

The **Babylonian method**, also known as **Heron's method**, is an ancient technique for approximating the square root of a number. It was known to Babylonian mathematicians as early as 1800 BC!

### 📏 The Method

Given a number `n`, and an initial guess `x₀`, the formula is:

\[
x_{n+1} = \frac{1}{2} \left(x_n + \frac{n}{x_n}\right)
\]

This is an **iterative method** that keeps improving the estimate until the change is very small.

### 💡 Algorithm

1. Choose an initial guess (e.g., `x₀ = n / 2` or `1.0`)
2. Repeat:
   - Compute: `x_{n+1} = (x_n + n / x_n) / 2`
   - Stop when `|x_{n+1} - x_n| < tolerance`

---

## 🐍 Python Implementation

```python
def babylonian_sqrt(n, guess=1.0, tolerance=1e-10, max_iterations=1000):
    """
    Babylonian method to approximate the square root of a number.

    Args:
        n (float): The number to find the square root of.
        guess (float): Initial guess (default is 1.0).
        tolerance (float): Stopping threshold.
        max_iterations (int): Maximum number of iterations.

    Returns:
        float: Approximated square root.
    """
    count = 0
    while count < max_iterations:
        next_guess = 0.5 * (guess + n / guess)
        if abs(next_guess - guess) < tolerance:
            return next_guess
        guess = next_guess
        count += 1
    return guess

# Example usage
if __name__ == "__main__":
    num = float(input("Enter a number: "))
    approx = babylonian_sqrt(num)
    print(f"Approximate square root of {num} is {approx:.10f}")
