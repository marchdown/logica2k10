#!/usr/bin/python
# -*- coding: utf-8 -*-
def check(s):
  m = "#"
  for i in range(len(s)):
    m += subst(s[i])
    if m in ["#(E+E)", "#(E*E)"]:
      m == "#"
    elif len(m)>len("#(E+E)"):
      print(u'некорректное выражение'.encode("UTF-8"))
      return(1)
  if m == "#":
      print(u'корректное выражение'.encode("UTF-8"))
      return(0)
  else:
      print(u'некорректное выражение'.encode("UTF-8"))
      return(1)

def subst(c):
  if c in "abE":
    return 'E'
  else: return c

def(main):
  if len(sys.argv) >= 2:
    expr = sys.argv[1]
  else:
    expr = "((a+b)*(a*b))"
  check(expr)

if __name__ == '__main__':
  main()
