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
  A = [(    a[i]) and (    b[i]) for i in l]
  B = [(not a[i]) and (    b[i]) for i in l]
  C = [(    a[i]) and (not b[i]) for i in l]
  D = [(not a[i]) and (not b[i]) for i in l]
  return map (sumTrue, (A, B, C, D))

def ff (a, b):
#  assert len(a) == len(b) == 100
# map (lambda x: not x, pBool)
  l = range(len(a))
  A = [(    a[i]) and (    b[i]) for i in l]
  B = [(not a[i]) and (    b[i]) for i in l]
  C = [(    a[i]) and (not b[i]) for i in l]
  D = [(not a[i]) and (not b[i]) for i in l]
  return  map (sumTrue, (A, B, C, D))

def tabulate():
  for i in range(len(gnames)):
    k1 = gnames[i]
    s1 = gd[k1]
    for j in range(len(gnames))[i+1:]:
      k2 = gnames[j]
      s2 = gd[k2]
      print k1, k2, f(s1, s2), otvet(s1, s2)

def otvet(a,b):
  A, B, C, D = f(a, b)
  if A*B == -D*C: return "fubar" # на ноль делить нельзя
  res = float(A*D - B*C)  / (A*D + B*C)
  return round_num(res)

genres = K, L, M, N, P, R
bgenres = bK, bL, bM, bN, bP, bR = map(parseStr, genres)
gnames = ['K', 'L', 'M', 'N', 'P', 'R']
# gn  = range(len(gnames))
gd = {'K':bK, 'L':bL, 'M':bM, 'N':bN, 'P':bP, 'R':bR}
# o = [(gnames[i], gnames[j], round_num(otvet(gd[gnames[i]], gd[gnames[j]]))) for i in gn for j in gn[i+1:]]
# q = [(k1, k2, otvet(gd[k1], gd[k2])) for k1 in gnames for k2 in gnames]
def round_num(num):
  res = float(int(num * 1000) ) / 1000
  return res

def printNums():
  for g in bgenres:
    print sumTrue(g)

def A(Key1, Key2):
  res = [Key1[i] and Key2[i] for i in range(len(Key1))]
  return res
def sort2(a, b):
  if a[2] > b[2]: return a, b
  else: return b, a

