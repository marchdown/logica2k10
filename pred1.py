# -*- coding: utf-8 -*-
from string import join as join
#import string

def buildp(m, n, args):
  return (m, n, args)

def renderp(p):
  return pp(p[0], p[1], p[2])

def printp(p):
  pr(p[0], p[1], p[2])

def pp(m, n, args):
  argstr = ''
  if n > 0:
    for i in range(n):
      argstr = argstr + "," + renderp(args[i])
#  else:
#    argstr = ""
  res = "F" + m*"₁"+ ";" + n*"₁"+ "(" + argstr + ")"
  return res

def pr(m, n, args):
  print pp(m, n, args)

def lp(maxlen):
## in glorius pseudocode:
## while len < maxlen
##  generate new sentence                             <— generate sencence?
##  if len(newsentence) < maxlen then add it to list
## print sort(list)
  return 0
def lp0(maxlen):
  res = []
  for i in range (maxlen-4):
    res.append(renderp((i, 0, [])))
    printp((i, 0, []))
  for i in range (maxlen-9):
    res.append(renderp(buildp(i, 1, [zerop])))
    printp((i, 1, [zerop]))
    # for q in res:
    #   a = renderp((i, 1, q))
    #   if len(a) < maxlen:
    #     print a
  for i in range (maxlen-11):
    printp((i, 2, [zerop, zerop]))
  for i in range (maxlen-16):
    printp((i, 3, [zerop, zerop, zerop]))
#  return res
def lp0helper():
  return 0
def lp1():
  return 0
zerop = (0, 0, '')
def incn(p):
  return(p[0]+1, p[1], p[2])

if __name__ == '__main__':
  main()
