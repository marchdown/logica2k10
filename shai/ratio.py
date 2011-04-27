#  R    /R
# QA  |  B
#  -------
#/QC  |  D
#  --     R       Q          R&Q  R/Q  Q/R  /(Q&R)
#  --     R       Q          A    B    C    D
#  f :: ([Bool], [Bool]) -> (Int, Int, Int, Int)
#  Main :: IO ()
#
#
##  R    /R
# R&Q | Q&/R
#  -------
# R&/Q|/Q&/R 
#
#
#
def f (a, b):
  assert len(a) == len(b) == 100
  l = range(100)
  A = [    a[i] and     b[i], for i in l]
  B = [    a[i] and not b[i], for i in l]
  C = [not a[i] and     b[i], for i in l]
  D = [not a[i] and not b[i], for i in l]
  return A, B, C, D

def ratio(a, b):
  A, B, C, D = f(a, b)
  res = (A*B - D*C) / (A*B + D*C)
  return res

