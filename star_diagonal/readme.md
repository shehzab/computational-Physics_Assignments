# Diagonal Sums: Nested Double Summation

A Python program that computes a nested double sum — $\sum_{i=1}^{n}\sum_{j=1}^{n} (i^2 + j^2)$ — using both a brute-force nested loop and a closed-form formula, and verifies the two agree.

---

## Overview

This project extends the single-variable [sum of squares](https://en.wikipedia.org/wiki/Squared_triangular_number) idea to two dimensions: instead of summing $i^2$ over a single index, it sums $i^2 + j^2$ over every pair $(i, j)$ in an $n \times n$ grid.

The program:

* Computes the double sum using two nested loops.
* Derives and computes the same result using a closed-form formula.
* Compares both results to confirm they match.

---

## Mathematical Background

The quantity being computed is:

$$
D(n) = \sum_{i=1}^{n}\sum_{j=1}^{n} \left(i^2 + j^2\right)
$$

### Deriving the Closed Form

The double sum can be split into two separate sums:

$$
D(n) = \sum_{i=1}^{n}\sum_{j=1}^{n} i^2 \; + \; \sum_{i=1}^{n}\sum_{j=1}^{n} j^2
$$

In the first term, $i^2$ doesn't depend on $j$, so the inner sum over $j$ just repeats it $n$ times:

$$
\sum_{i=1}^{n}\sum_{j=1}^{n} i^2 = \sum_{i=1}^{n} n \cdot i^2 = n \sum_{i=1}^{n} i^2
$$

By symmetry, the second term equals the same thing:

$$
\sum_{i=1}^{n}\sum_{j=1}^{n} j^2 = n \sum_{j=1}^{n} j^2
$$

Adding them together:

$$
D(n) = 2n \sum_{k=1}^{n} k^2
$$

Substituting the sum-of-squares formula $\sum_{k=1}^{n} k^2 = \dfrac{n(n+1)(2n+1)}{6}$:

$$
D(n) = 2n \cdot \frac{n(n+1)(2n+1)}{6}
$$

This is exactly what `diagonal_sum_formula(n)` computes — reusing `sum_squares_formula(n)` rather than re-deriving the inner formula.

---

## Program Structure

### 1. `sum_squares_formula(n)`

The familiar closed-form sum of squares, reused as a building block:

```python
def sum_squares_formula(n):
    return n * (n + 1) * (2 * n + 1) // 6
```

$$
\sum_{k=1}^{n} k^2 = \frac{n(n+1)(2n+1)}{6}
$$

---

### 2. `diagonal_sum(n)`

Computes $D(n)$ directly with a nested loop over every $(i, j)$ pair:

```python
def diagonal_sum(n):
    total = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            total += i ** 2 + j ** 2
    return total
```

This visits all $n^2$ pairs and adds $i^2 + j^2$ for each one — a direct, unoptimized translation of the double summation.

---

### 3. `diagonal_sum_formula(n)`

Computes the same value analytically, using the derivation above:

```python
def diagonal_sum_formula(n):
    return 2 * n * sum_squares_formula(n)
```

$$
D(n) = 2n \cdot \frac{n(n+1)(2n+1)}{6}
$$

Instead of $n^2$ additions, this computes the result in a constant number of arithmetic operations.

---

## Verification

Running the program computes both versions for $n = 50$ and checks they match:

```python
n = 50
loop_val = diagonal_sum(n)
formula_val = diagonal_sum_formula(n)
print(f"diagonal_sum({n}) = {loop_val}")
print(f"diagonal_sum_formula({n}) = {formula_val}")
print(f"Match? {loop_val == formula_val}")
```

### Sample Output

```text
diagonal_sum(50) = 4292500
diagonal_sum_formula(50) = 4292500
Match? True
```

*(Verified by running the script for n = 5, 50, and 100 — all three matched.)*

---

## Time Complexity

### Loop Method

The nested loop visits every $(i, j)$ pair in an $n \times n$ grid:

$$
O(n^2)
$$

Runtime grows quadratically with $n$, since there are $n^2$ total additions.

### Formula Method

The formula performs a fixed number of arithmetic operations regardless of $n$:

$$
O(1)
$$

This is a much larger speedup than the single-sum case, since it replaces $n^2$ operations with a constant number — not just $n$.

---

## Concepts Demonstrated

* Nested Summation / Double Sums
* Separating and Simplifying Double Sums
* Reuse of Closed-Form Building Blocks
* Algorithm Verification
* Time Complexity: $O(n^2)$ vs. $O(1)$
* Python Functions and Nested Loops

---

## Requirements

* Python 3.x
* No external libraries required

---

## Learning Outcomes

After studying this project, you should understand:

1. How to reason about and simplify a nested double summation.
2. Why $i^2$ can be pulled out of a sum over $j$ when it doesn't depend on $j$.
3. How to reuse an existing closed-form formula as a building block for a more complex one.
4. The difference between $O(n^2)$ and $O(1)$ algorithms, and why it matters more as $n$ grows.
5. How to verify an analytical formula against a brute-force implementation.

---

## File Name

```text
diagonal_sum.py
```

---

## Author

**Sinan Shehzab**
BSc Physics | Computational Mathematics & Python Programming