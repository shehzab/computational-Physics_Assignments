"""
SECTION C - Convergence loop: bisection square root
"""
import math 
def sqrt_bisection(n, tol=1e-6):
    """Return (sqrt_estimate, n_iterations) for sqrt(n) using bisection on the interval [0, max(n,1)] until the interval width < tol."""

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


if __name__ == "__main__":

    print(f"{'n':>6} | {'bisection sqrt':>16} | {'math.sqrt':>16} | {'iterations':>10}")
    print("-" * 58)

    for n in (2, 7, 100):
        est, iters = sqrt_bisection(n)
        print(f"{n:>6} | {est:>16.8f} | {math.sqrt(n):>16.8f} | {iters:>10}")


# Output:
#      n |   bisection sqrt |       math.sqrt | iterations
# ----------------------------------------------------------
#      2 |       1.41421366 |       1.41421356 |         21
#      7 |       2.64575124 |       2.64575131 |         23
#    100 |      10.00000000 |      10.00000000 |         27