"""
SECTION B - Numerical summation: sum of squares
"""

def sum_squares(n):
  """Return the accumulated sum of k^2 for k = 1..n."""
  total = 0
  for k in range(1, n + 1):
    total += k** 2
  return total

def sum_squares_formula(n):
  """Return n(n+1)(2n+1)/6, the closed form formula for sum of squares"""
  return n * (n+1)*(2*n+1)//6

if __name__ == "__main__":
  print(f"{'n':>6} | {'sum_squares(loop)':>20} | {'match?':7}")
  print("-"* 62)
  for n in (10, 100, 1000):
    loop_val = sum_squares(n)
    formula_val = sum_squares_formula(n)
    print(f"{n:>6} | {loop_val:>20} | {formula_val:>20} | {loop_val == formula_val!s:>7}")


# Output

#        n |    sum_squares(loop) | match? 
#--------------------------------------------------------------
#   10 |                  385 |                  385 |    True
#   100 |               338350 |               338350 |    True
#  1000 |            333833500 |            333833500 |    True