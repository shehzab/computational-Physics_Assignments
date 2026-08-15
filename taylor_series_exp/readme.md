# Taylor Series Approximation of $e^x$

A Python implementation of the Taylor Series expansion for approximating the exponential function $e^x$. This project demonstrates how infinite series can be used in numerical computation and how the approximation improves as more terms are included.

---

## Overview

The exponential function $e^x$ is one of the most important functions in mathematics, physics, engineering, and computer science. Although Python provides the built-in `math.exp(x)` function, this project demonstrates how the same result can be approximated using a Taylor Series.

The program:

* Approximates $e^x$ using the Taylor Series expansion.
* Compares the approximation with Python's `math.exp(x)`.
* Calculates the approximation error.
* Shows how the approximation converges as more terms are added.

---

## Mathematical Background

The Taylor Series expansion of the exponential function is:

$$
e^x = \sum_{k=0}^{\infty}\frac{x^k}{k!}
$$

Expanded form:

$$
e^x = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \frac{x^4}{4!} + \cdots
$$

where:

* $x$ is the input value.
* $k$ is the term number.
* $k!$ denotes the factorial of $k$.

The factorial function is defined as:

$$
n! = n(n-1)(n-2)\cdots2\cdot1
$$

Examples:

* $0! = 1$
* $1! = 1$
* $2! = 2$
* $3! = 6$
* $4! = 24$

Since the series contains infinitely many terms, a computer approximates the value by summing only a finite number of terms.

---

## Example: Approximating $e$

For $x = 1$:

$$
e = e^1
$$

Using the first five terms:

$$
e \approx 1 + 1 + \frac{1}{2} + \frac{1}{6} + \frac{1}{24} \approx 2.7083333333
$$

Actual value:

$$
e \approx 2.7182818285
$$

As more terms are added, the approximation becomes increasingly accurate.

---

## How the Program Works

### Step 1: Initialize the First Term

The Taylor Series begins with:

$$
T_0 = \frac{x^0}{0!} = 1
$$

The program initializes:

```python
total = 0.0
term = 1.0
```

* `term` stores the current Taylor Series term.
* `total` stores the running sum of all terms.

---

### Step 2: Add Each Term to the Sum

For every iteration:

```python
total += term
```

Mathematically:

$$
S_n = \sum_{k=0}^{n-1} T_k
$$

where

$$
T_k = \frac{x^k}{k!}
$$

and $S_n$ is the approximation after $n$ terms.

---

### Step 3: Generate the Next Term Efficiently

A straightforward implementation would repeatedly calculate:

$$
\frac{x^k}{k!}
$$

for every value of $k$. Instead, this program uses a recurrence relation, which is faster because it builds each new term from the previous one instead of recomputing a power and a factorial from scratch every time.

Let:

$$
T_k = \frac{x^k}{k!} \quad \text{and} \quad T_{k+1} = \frac{x^{k+1}}{(k+1)!}
$$

Dividing the two expressions:

$$
\frac{T_{k+1}}{T_k} = \frac{\dfrac{x^{k+1}}{(k+1)!}}{\dfrac{x^k}{k!}}
$$

Simplifying:

$$
\frac{T_{k+1}}{T_k} = \frac{x}{k+1}
$$

Therefore:

$$
T_{k+1} = T_k \times \frac{x}{k+1}
$$

This relation is implemented in Python as:

```python
term *= x / (k + 1)
```

This avoids repeated power and factorial calculations, making the algorithm more efficient.

---

## Error Analysis

To evaluate the accuracy of the approximation, the result is compared with Python's built-in exponential function.

True value:

$$
e^x = \operatorname{exp}(x)
$$

Absolute error is defined as the magnitude of the difference between the approximated value and the true value:

$$
\text{Absolute Error} = \left| A - T \right|
$$

where:

* $A$ = Approximated value
* $T$ = True value

In this program:

```python
A = approx_exp(x, n)
T = math.exp(x)
```

The error is calculated as:

```python
abs(approx_exp(x, n) - math.exp(x))
```

As the number of terms increases:

$$
\text{Error} \rightarrow 0
$$

which demonstrates the convergence of the Taylor Series.

---

## Functions

### `approx_exp(x, n_terms)`

Computes the Taylor Series approximation:

$$
\sum_{k=0}^{n-1}\frac{x^k}{k!}
$$

#### Parameters

| Parameter | Description                          |
| --------- | ------------------------------------ |
| `x`       | Input value                          |
| `n_terms` | Number of Taylor Series terms to use |

#### Returns

Approximation of $e^x$.

---

### `error_table(x, max_n_terms)`

Generates a table containing:

* Number of terms used.
* Approximation value.
* Absolute error.

This makes it easy to observe how the approximation improves as additional terms are included.

---

## Sample Output

```text
approx_exp(1, 20) = 2.7182818285
math.exp(1)       = 2.7182818285
Match to 10 decimal places? True
```

Example error table:

```text
 n_terms |        approx_exp |      abs error
----------------------------------------------
       1 |     1.000000000000 |      1.718e+00
       2 |     2.000000000000 |      7.183e-01
       3 |     2.500000000000 |      2.183e-01
       4 |     2.666666666667 |      5.162e-02
       5 |     2.708333333333 |      9.948e-03
      ...
      20 |     2.718281828459 |      ~0
```

---

## Computational Advantage

### Naive Approach

Compute each term independently:

$$
\frac{x^k}{k!}
$$

This requires repeated calculations of:

* Powers
* Factorials

for every term.

### Optimized Approach (Used in This Project)

Use the recurrence relation:

$$
T_{k+1} = T_k \times \frac{x}{k+1}
$$

Advantages:

* Fewer calculations.
* Faster execution.
* Better computational efficiency.
* Reduced overhead for large numbers of terms.

---

## Concepts Demonstrated

* Taylor Series Expansion
* Infinite Series
* Numerical Approximation
* Error Analysis
* Factorials
* Recurrence Relations
* Convergence of Series
* Computational Mathematics
* Python Functions and Loops

---

## Requirements

Python 3.x

Required module:

```python
import math
```

---

## Learning Outcomes

After studying this project, you should understand:

1. How the exponential function can be represented using an infinite series.
2. How Taylor Series approximations work.
3. Why approximation accuracy improves as more terms are added.
4. How recurrence relations improve computational efficiency.
5. How numerical methods are implemented in Python.
6. How approximation error is measured and analyzed.

---

## File Name

```text
taylor_exp_approximation.py
```

---

## Author

**Sinan Shehzab**
BSc Physics | Computational Mathematics & Web Development