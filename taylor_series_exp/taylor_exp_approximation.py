"""
SECTION A - Infinite series: e^x via Taylor expansion
"""

import math


def approx_exp(x, n_terms):
    """Return the Taylor-series approximation of e^x using n_terms terms."""
    total = 0.0
    term = 1.0

    for k in range(n_terms):
        total += term
        term *= x / (k + 1)

    return total


def error_table(x, max_n_terms):
    """Print n_terms, approximation, and absolute error."""
    true_value = math.exp(x)

    print(f"\nError vs n_terms for e^{x}")
    print(f"{'n_terms':>8} | {'approx_exp':>18} | {'abs error':>14}")
    print("-" * 46)

    for n in range(1, max_n_terms + 1):
        approx = approx_exp(x, n)
        error = abs(approx - true_value)

        print(f"{n:8} | {approx:18.12f} | {error:14.3e}")


if __name__ == "__main__":
    approx = approx_exp(1, 20)
    true_value = math.exp(1)

    print(f"approx_exp(1, 20) = {approx:.10f}")
    print(f"math.exp(1)       = {true_value:.10f}")
    print(f"Match to 10 decimal places? {round(approx, 10) == round(true_value, 10)}")

    error_table(1, 20)


# OUTPUT:
# approx_exp(1, 20) = 2.7182818285
# math.exp(1)       = 2.7182818285
# Match to 10 decimal places? True
#
# Error vs n_terms for e^1
#  n_terms |         approx_exp |      abs error
# ----------------------------------------------
#        1 |     1.000000000000 |      1.718e+00
#        2 |     2.000000000000 |      7.183e-01
#        3 |     2.500000000000 |      2.183e-01
#        4 |     2.666666666667 |      5.162e-02
#        5 |     2.708333333333 |      9.948e-03
#        6 |     2.716666666667 |      1.615e-03
#        7 |     2.718055555556 |      2.263e-04
#        8 |     2.718253968254 |      2.786e-05
#        9 |     2.718278769841 |      3.059e-06
#       10 |     2.718281525573 |      3.029e-07
#       11 |     2.718281801146 |      2.731e-08
#       12 |     2.718281826198 |      2.261e-09
#       13 |     2.718281828286 |      1.729e-10
#       14 |     2.718281828447 |      1.229e-11
#       15 |     2.718281828458 |      8.149e-13
#       16 |     2.718281828459 |      5.018e-14
#       17 |     2.718281828459 |      2.220e-15
#       18 |     2.718281828459 |      4.441e-16
#       19 |     2.718281828459 |      4.441e-16
#       20 |     2.718281828459 |      4.441e-16