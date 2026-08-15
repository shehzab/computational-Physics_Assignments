# Bisection Method: Approximating Square Roots

A Python implementation that approximates $\sqrt{n}$ using the **bisection method** — a simple numerical technique that repeatedly halves a search interval until it converges on the answer.

---

## Overview

Instead of computing $\sqrt{n}$ directly, this program searches for it by narrowing down a range of possible values. It starts with an interval that is guaranteed to contain $\sqrt{n}$, then repeatedly checks the midpoint and shrinks the interval based on whether the midpoint is too high or too low.

The program:

* Approximates $\sqrt{n}$ using bisection.
* Compares the result with Python's built-in `math.sqrt(n)`.
* Reports how many iterations the method took to converge.

---

## Mathematical Background

To find $\sqrt{n}$, we look for a value $x$ such that:

$$
x^2 = n
$$

The bisection method starts with an interval $[\text{lo}, \text{hi}]$ known to contain the answer, then repeatedly:

1. Computes the midpoint:

$$
\text{mid} = \frac{\text{lo} + \text{hi}}{2}
$$

2. Checks whether $\text{mid}^2$ is greater than or less than $n$:

   * If $\text{mid}^2 > n$, the true root is smaller, so set $\text{hi} = \text{mid}$.
   * Otherwise, the true root is larger (or equal), so set $\text{lo} = \text{mid}$.

3. Repeats until the interval is narrower than a tolerance value:

$$
\text{hi} - \text{lo} < \text{tol}
$$

Each iteration cuts the interval in half, so the method converges quickly — this is known as **linear convergence with ratio $\tfrac{1}{2}$**.

---

## Choosing the Initial Interval

The search starts at:

$$
\text{lo} = 0, \qquad \text{hi} = \max(n, 1)
$$

This guarantees the interval contains $\sqrt{n}$ for any $n \geq 0$:

* For $n \geq 1$, $\sqrt{n} \leq n$, so `hi = n` is a safe upper bound.
* For $0 \leq n < 1$, $\sqrt{n} \leq 1$, so `hi = 1` is used instead (since $n$ itself would be too small an upper bound).

---

## Function: `sqrt_bisection(n, tol=1e-6)`

Computes an approximation of $\sqrt{n}$ using bisection.

#### Parameters

| Parameter | Description                                      |
| --------- | ------------------------------------------------- |
| `n`       | The non-negative number to take the square root of |
| `tol`     | The interval width at which the loop stops (default `1e-6`) |

#### Returns

A tuple `(sqrt_estimate, n_iterations)`:

* `sqrt_estimate` — the midpoint of the final interval, used as the approximation of $\sqrt{n}$.
* `n_iterations` — the number of times the interval was halved.

#### Errors

Raises a `ValueError` if `n` is negative, since square roots of negative numbers aren't defined over the reals.

---

## Sample Output (intended)

```text
     n |  bisection sqrt |       math.sqrt | iterations
----------------------------------------------------------
     2 |      1.41421354 |       1.41421356 |         21
     7 |      2.64575136 |       2.64575131 |         23
   100 |     10.00000000 |      10.00000000 |         27
```

*(Exact iteration counts depend on the initial interval width and `tol`.)*

---

## Time Complexity

Each iteration halves the interval, so the number of iterations needed to reach a tolerance `tol` from a starting width `W` is:

$$
\text{iterations} \approx \log_2\left(\frac{W}{\text{tol}}\right)
$$

This gives the algorithm a time complexity of:

$$
O(\log(1/\text{tol}))
$$

which is very fast compared to naive linear search methods.

---

## Known Issues

The current code has two bugs that should be fixed before use:

1. **`return` is inside the `while` loop.** As written, the function exits after the very first iteration instead of looping until the interval shrinks below `tol`. The `return (lo+hi)/2, iterations` line should be dedented so it sits *after* the loop, not inside it.
2. **`valueError` should be `ValueError`.** Python's built-in exception class is capitalized; as written this will raise a `NameError` instead of the intended `ValueError` when `n < 0`.

Fixed version of the affected section:

```python
def sqrt_bisection(n, tol=1e-6):
    if n < 0:
        raise ValueError("n must be non-negative")
    lo, hi = 0.0, max(n, 1.0)
    iterations = 0
    while (hi - lo) > tol:
        mid = (lo + hi) / 2
        if mid * mid > n:
            hi = mid
        else:
            lo = mid
        iterations += 1
    return (lo + hi) / 2, iterations
```

---

## Concepts Demonstrated

* Bisection Method / Binary Search on Real Numbers
* Numerical Root-Finding
* Convergence and Tolerance
* Iterative Algorithms
* Python Functions and Loops
* Error Handling with Exceptions

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

1. How the bisection method narrows in on a numerical answer.
2. Why the choice of initial interval matters for correctness.
3. How a tolerance value controls precision vs. iteration count.
4. The logarithmic time complexity of bisection-based algorithms.
5. How to validate input and raise appropriate exceptions in Python.

---

## File Name

```text
sqrt_bisection.py
```