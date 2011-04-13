#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys, re

# def build_table(G):
#   res = []
  
#   return res

# G0 = """
# E->E+T | T
# T->T*F | F
# F->(E) | a
# """
G = [("E", "E+T"),("E", "T"),("T", "T*F"),("T", "F"),("F", "(E)"),("F", "a")]

def validate(s):
  m = "#"
  p = 0
  for i in range(len(s)):
    x = m[-1]
    y = s[i]
    if not greater(x, y):
      m += y
      # break from for cycle
    elif greater(x,y):
      m = sverni(m) # there are no procedures in python
      # FIXME: check if m is changed 
      # break from for cycle
#    elif nesravnimo(x,y):
      # break from cycle
  #end cycle
  return m == "#E"
def recursive_sverni(s):
  res = sverni(s)
  print res
  if res == s:
    return res # break
    print 'idempotency reached'
  res = recursive_sverni(res)
  return res
DEBUG = True
def sverni(s):
  res = s
  for i in range(len(res)):

    if DEBUG: print 'applying rules to', s[-i:]
    for rule in G:
      if DEBUG: print 'trying rule', rule
      if rule[1] == s[-i:]:  # check bounds
        if DEBUG: print 'replacing',s[-i:],'with',rule[0]
        res = s[:-i] + rule[0]
        break #return res
    if res != s: 
      if DEBUG: print 'done'
      break

  return res

def sravni(x,y):
  str2 = "abcd"
  str3 = "fbde"
  p_x = str2.find(x)
  p_y = str2.find(y)
  if p_x > p_y:
    print x, '>', y
  else:
    print x, '<', y


# #    E  T  F  a  (  )  +  *  #
# G1= [[],[],[],[],[],[=],[=],[],[],  #E
#      [],[],[],[],[],[>],[>],[=],[>],  #T
#      [],[],[],[],[],[],[],[],[],  #F
#      [],[],[],[],[],[],[],[],[],  #a
#      [],[],[],[],[],[],[],[],[],  #(
#      [],[],[],[],[],[],[],[],[],  #)
#      [],[],[],[],[],[],[],[],[],  #+
#      [],[],[],[],[],[],[],[],[],  #*
#      [],[],[],[],[],[],[],[],[]]  ##

# #     E    T    F    a    (    )    +    *    #
# G2= [[  ],[  ],[  ],[  ],[  ],[  ],[  ],[  ],[  ],  #E
#      [  ],[  ],[  ],[  ],[  ],[  ],[  ],[  ],[  ],  #T
#      [  ],[  ],[  ],[  ],[  ],[  ],[  ],[  ],[  ],  #F
#      [  ],[  ],[  ],[  ],[  ],[  ],[  ],[  ],[  ],  #a
#      [  ],[  ],[  ],[  ],[  ],[  ],[  ],[  ],[  ],  #(
#      [  ],[  ],[  ],[  ],[  ],[  ],[  ],[  ],[  ],  #)
#      [  ],[  ],[  ],[  ],[  ],[  ],[  ],[  ],[  ],  #+
#      [  ],[  ],[  ],[  ],[  ],[  ],[  ],[  ],[  ],  #*
#      [  ],[  ],[  ],[  ],[  ],[  ],[  ],[  ],[  ]]  ##

# #     E    T    F    a    (    )    +    *    #
# G3= [[  ],[  ],[  ],[  ],[  ],[= ],[= ],[  ],[  ],  #E
#      [  ],[  ],[  ],[  ],[  ],[> ],[> ],[= ],[> ],  #T
#      [  ],[  ],[  ],[  ],[  ],[> ],[> ],[> ],[> ],  #F
#      [  ],[  ],[  ],[  ],[  ],[> ],[> ],[> ],[> ],  #a
#      [  ],[  ],[  ],[  ],[  ],[> ],[> ],[> ],[> ],  #(
#      [<,=],[<],[< ],[< ],[< ],[  ],[  ],[  ],[  ],  #)
#      [  ],[<,=],[<],[< ],[< ],[  ],[  ],[  ],[  ],  #+
#      [  ],[= ],[= ],[< ],[< ],[  ],[  ],[  ],[  ],  #*
#      [< ],[< ],[< ],[< ],[< ],[  ],[  ],[  ],[  ]]  ##


################################################################################
#	Дальше идут проверки

def main():
  return 0

if __name__ == '__main__':
  main()
