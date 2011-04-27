#!/usr/bin/python
# -*- coding: utf-8 -*-
#
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

def otvet(a,b):
  A, B, C, D = f(a, b)
  if A*B == -D*C: return "fubar" # на ноль делить нельзя
  res = float(A*B - D*C)  / (A*B + D*C)
  return  res

genres = K, L, M, N, P, R
bgenres = bK, bL, bM, bN, bP, bR = map(parseStr, genres)
gnames = ['K', 'L', 'M', 'N', 'P', 'R']
o = [otvet(i, j) for i in bgenres for j in bgenres]

def printNums():
  for g in bgenres:
    print sumTrue(g)

def A(Key1, Key2):
  res = [Key1[i] and Key2[i] for i in range(len(Key1))]
  return res
  
# data
#   01         11        21        31        41        51        61        71        81        91       100 
#   !#         #         #         #         #         #         #         #         #         #        !#
K = 'ttttftfftfttffffftftftfffftttfffftfffftttfttfttfftffttfttttftftttttttfftfftftffttttfttfttttftttftftf'
L = 'ttttfftftfttffffttftftftfttftffffttftfftfftttttfffffttfttttttftttttttfftfftftffttttfttfttttftttftftt'
M = 'fftt--.--.ttf.ffttftftftftt.tfff.ttftf.t.ft--ttfffffttftttt-tftttttttfftfftftffttttfttftttt.ttt.tftt'
N = 'ttttftfftfftffftftftftftfttftftfftfffffttftftttfffffttfttttttftttttttfftfftftffttttfttfttttffttftftt' # ?
P = 'ttttftfftfttffffttftftffftttfftfftfffffttfttfttfftffttfttttttftttttttfftfftftffttttfttfttttftttftftt'
R = 'ttttttfttfftffffftftftftftfttftfftfftftftftftttfttfftffttttttftttttttfftfftftfttttttttftttttftfftttt'
#   01         11        21        31        41        51        61        71        81        91       100 
#   !#         #         #         #         #         #         #         #         #         #        !#
