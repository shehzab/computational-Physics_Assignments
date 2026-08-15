"""
SECTION A - Infinite series: e^x via Taylor expansion
"""
import math

def approx_exp(x,n_terms):
  """ Return the Taylor-series approximation of e^x using n_terms terms
    (sum of x^k / k! for k = 0 .. n_terms-1) """

  total = 0.0
  term = 1.0
  for k in range(n_terms):
    total += term
    " total += (x ** k) / math.factorial(k)"
    term *= x / ( k + 1 )

  return total

def error_table(x, max_n_terms):
  """Print a table of n_terms vs absolute error | approx_exp - math.exp(x)|"""
  print(f"\nError vs n_terms for e^{x} (true value = {math.exp(x):.12f})")
  print(f"{'n_terms':>8} | {'approx_exp':>18} | { 'abs error':>14} ")
  print("-"*46)
  for n in range(1, max_n_terms + 1):
    approx = approx_exp(x, n)
    err = abs(approx - math.exp(x))
    print(f"{n:8} | {approx:> 18.12f} | {err:>14.3e}")

if __name__ == "__main__":
  approx = approx_exp(1, 20)
  true_val = math.exp(1)
  print(f"approx_exp(1, 20) = {approx:.10f}")
  print(f"math.exp(1) = {true_val:.10f}")
  print(f"Match to 10 decimal places? {round(approx,10) ==  round(true_val, 10)}")
  error_table(1,20)