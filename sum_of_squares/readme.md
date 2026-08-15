# Numerical Summation: Sum of Squares

A Python program that calculates the sum of the squares of the first **n natural numbers** using two different approaches:

1. An iterative (loop-based) method
2. A direct mathematical formula

The program verifies that both approaches produce the same result.

---

## Overview

The sum of squares is a well-known mathematical series:

$$
1^2 + 2^2 + 3^2 + \cdots + n^2
$$

This project demonstrates how a mathematical problem can be solved both computationally and analytically.

The program:

* Computes the sum using a loop.
* Computes the same sum using a mathematical formula.
* Compares both results.
* Demonstrates the efficiency of a closed-form solution.

---

## Mathematical Background

The sum of the squares of the first $n$ natural numbers can be written using summation notation:

$$
\sum_{k=1}^{n} k^2
$$

A closed-form formula exists for this series:

$$
\sum_{k=1}^{n} k^2 = \frac{n(n+1)(2n+1)}{6}
$$

where:

* $n$ = number of terms
* $k$ = term index

This formula allows us to calculate the result directly without repeatedly adding each square.

---

## Example

For $n = 5$, the numerical summation is:

$$
1^2 + 2^2 + 3^2 + 4^2 + 5^2 = 1 + 4 + 9 + 16 + 25 = 55
$$

Using the formula:

$$
\frac{5(5+1)(2\times5+1)}{6} = \frac{5\times6\times11}{6} = 55
$$

Both approaches produce the same result.

---

## Program Structure

### 1. `sum_squares(n)`

This function calculates the sum of squares using a loop.

```python
def sum_squares(n):
    total = 0
    for k in range(1, n + 1):
        total += k**2
    return total
```

#### Algorithm

1. Initialize a running total.
2. Loop from 1 to $n$.
3. Square each value.
4. Add the square to the running total.
5. Return the final result.

Mathematically:

$$
S = \sum_{k=1}^{n} k^2
$$

---

### Example Execution

For $n = 5$:

| k | $k^2$ | Running Total |
| - | ----: | ------------: |
| 1 |     1 |             1 |
| 2 |     4 |             5 |
| 3 |     9 |            14 |
| 4 |    16 |            30 |
| 5 |    25 |            55 |

Final result:

$$
S = 55
$$

---

### 2. `sum_squares_formula(n)`

This function uses the closed-form mathematical formula.

```python
def sum_squares_formula(n):
    return n * (n + 1) * (2 * n + 1) // 6
```

Mathematical formula:

$$
\sum_{k=1}^{n} k^2 = \frac{n(n+1)(2n+1)}{6}
$$

Instead of performing *n* additions, the answer is computed directly.

---

## Why Use Integer Division?

The formula always produces a whole number for positive integers.

```python
// 6
```

ensures that the result remains an integer.

Example:

$$
\frac{330}{6} = 55
$$

Result:

```python
55
```

instead of:

```python
55.0
```

---

## Verification Process

The program tests the following values:

$$
n = 10,\quad 100,\quad 1000
$$

For each value:

1. Calculate the result using the loop method.
2. Calculate the result using the formula method.
3. Compare both values.

Verification condition:

$$
\text{Loop Result} = \text{Formula Result}
$$

If the values match, the program prints:

```python
True
```

---

## Sample Output

```text
     n |    sum_squares(loop) |              formula |  match?
--------------------------------------------------------------
    10 |                  385 |                  385 |    True
   100 |               338350 |               338350 |    True
  1000 |            333833500 |            333833500 |    True
```

---

## Time Complexity

### Loop Method

The loop executes once for every value from 1 to $n$.

Complexity:

$$
O(n)
$$

As *n* increases, execution time increases proportionally.

---

### Formula Method

The formula performs a fixed number of arithmetic operations.

Complexity:

$$
O(1)
$$

Execution time remains constant regardless of the value of *n*.

---

## Why This Project Matters

This project demonstrates:

* Numerical summation
* Mathematical series
* Closed-form formulas
* Verification of mathematical identities
* Algorithm efficiency
* Time complexity analysis

It is a simple but powerful example of how mathematics can reduce computational effort.

---

## Concepts Demonstrated

* Summation Notation
* Series and Sequences
* Sum of Squares Formula
* Numerical Methods
* Algorithm Verification
* Time Complexity
* Python Functions
* Iteration and Loops

---

## Requirements

* Python 3.x
* No external libraries required

---

## Learning Outcomes

After completing this project, you should understand:

1. How to calculate a numerical summation using loops.
2. How the sum of squares formula works.
3. The difference between iterative and closed-form solutions.
4. Why mathematical formulas can significantly improve efficiency.
5. How to verify mathematical results using programming.
6. The difference between $O(n)$ and $O(1)$ algorithms.

---

## Suggested File Name

```text
sum_of_squares.py
```

Alternative names:

```text
numerical_summation.py
sum_squares_verification.py
sum_of_squares_formula.py
```

---

## Author

**Sinan Shehzab**
BSc Physics | Computational Mathematics & Python Programming