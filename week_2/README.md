# 📘 Week 2: Error Analysis in Numerical Computation

This week focuses on understanding and analyzing errors that arise in numerical computations. Accurate numerical analysis is crucial for developing reliable algorithms and ensuring the precision of computational results.

## 📂 Files Overview

### 1. `compute-absolute-and-relative-errors.py`

**Purpose:**  
Demonstrates how to calculate absolute and relative errors between an approximate value and the true value.

**Key Concepts:**

- **Absolute Error:**  
  The absolute difference between the true value and the approximate value.
  
$$
\text{Absolute Error} = | \text{True Value} - \text{Approximate Value} |
$$

- **Relative Error:**  
  The absolute error divided by the true value, providing a sense of the error's size relative to the true value.
  
  $$
  \text{Relative Error} = \frac{\text{Absolute Error}}{|\text{True Value}|}
  $$

**Usage:**

This script can be used to understand how errors are quantified in numerical methods, which is essential for assessing the accuracy of computational algorithms.

### 2. `precision-loss-in-fractions.py`

**Purpose:**  
Illustrates the loss of precision that can occur when performing arithmetic operations with floating-point numbers, especially when subtracting nearly equal numbers.

**Key Concepts:**

- **Floating-Point Arithmetic:**  
  Computers represent real numbers approximately due to finite precision, which can lead to rounding errors.

- **Catastrophic Cancellation:**  
  Significant digits can be lost when subtracting two nearly equal numbers, leading to a large relative error.

**Usage:**

By running this script, one can observe how certain operations can lead to significant precision loss, emphasizing the importance of numerical stability in algorithm design.

## 🧠 Learning Outcomes

- Understand the definitions and significance of absolute and relative errors.
- Recognize scenarios where floating-point arithmetic can lead to significant precision loss.
- Appreciate the importance of error analysis in developing robust numerical algorithms.

## 🚀 Getting Started

To run the scripts:

```bash
python compute-absolute-and-relative-errors.py
python precision-loss-in-fractions.py
