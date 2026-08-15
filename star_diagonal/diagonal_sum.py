"""
STRETCH - Diagonal sums: nested accumulator
"""

def sum_squares_formula(n):
  """Return n(n+1)(2n+1)/6, the closed-form formula for sum of squares."""
  return n * (n + 1) * (2 * n + 1) // 6

def diagonal_sum(n):
  """Return the nested double sum: sun_i sum_j (i^2 + j^2) for i, j = 1..n."""
  total = 0
  for i in range(1, n + 1):
    for j in range(1, n + 1):
      total += i ** 2 + j ** 2
  return total

def diagonal_sum_formula(n):
  """Return the analytical result 2*n*n(n+1)(2n+1)/6 for the diagonal double sum."""
  return 2 * n * sum_squares_formula(n)

if __name__ == "__main__":
  n = 50
  loop_val = diagonal_sum(n)
  formula_val = diagonal_sum_formula(n)
  print(f"diagonal_sum({n}) = {loop_val}")
  print(f"diagonal_sum_formula({n}) = {formula_val}")
  print(f"Match? {loop_val == formula_val}")