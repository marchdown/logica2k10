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
def parseStr(s):
  res = []
  for c in s:
    if c in 't+y.':
      res.append(True)
    else:
      res.append(False)
  return res

def sumTrue(arr):
  res = 0
  for v in arr:
    if v:
      res += 1
  return res
def f (a, b):
#  assert len(a) == len(b) == 100
# map (lambda x: not x, pBool)
  l = range(len(a))
  A = [    a[i] and     b[i] for i in l]
  B = [    a[i] and not b[i] for i in l]
  C = [not a[i] and     b[i] for i in l]
  D = [not a[i] and not b[i] for i in l]
  return map (sumTrue, (A, B, C, D))

def ratio(a, b):
  A, B, C, D = f(a, b)
  if A*B == -D*C: return "fubar" # на ноль делить нельзя
  res = (A*B - D*C) / (A*B + D*C)
  return res


# data
#   01         11        21        31        41        51        61        71        81        91       100 
#   !#         #         #         #         #         #         #         #         #         #        !#
K = 'ttttftfftfttffffftftftfffftttfffftfffftttfttfttfftffttfttttftftttttttfftfftftffttttfttfttttftttftftf'
L = 'ttttfftftfttffffttftftftfttftffffttftfftfftttttfffffttfttttttftttttttfftfftftffttttfttfttttftttftftt'
M = 'fftt--.--.ttf.ffttftftftftt.tfff.ttftf.t.ft--ttfffffttftttt-tftttttttfftfftftffttttfttftttt.ttt.tftt'
N = 'ttttftfftfftffftftftftftfttftftfftfffffttftftttfffffttfttttttfttttttttftfftftffttttfttfttttffttftftt'
P = 'ttttftfftfttffffttftftffftttfftfftfffffttfttfttfftffttfttttttfttttttttftfftftffttttfttfttttftttftftt'
R = 'ttttttfttfftffffftftftftftfttftfftfftftftftftttfttfftffttttttftttttttfftfftftfttttttttftttttftfftttt'
#   01         11        21        31        41        51        61        71        81        91       100 
#   !#         #         #         #         #         #         #         #         #         #        !#
