#!/usr/bin/python
# -*- coding: utf-8 -*-
<<<<<<< HEAD
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


=======
import sys

def build_table(G):
  return ''
def derive_string(s):
  p = 0                   # каретка
  m = "#"
  for i in range(len(s)):
    x = m[-1]
    y = s[i]
    if T(x, y) in "<=":
      m += y
    elif:
      m = sverni(m)
  if


def T(a, b):
  return G[a][b]

def ab2E(c):
  if c in "abE":
    return 'E'
  else:
    return c
################################################################################
#	Дальше идут проверки
#	
#	Проверки устроены так: 
#	Заранее задан массив кортежей вида (выражение, результат)
#	Все выражения по-очереди оцениваются на корректность
#       Результаты сравниваются с заданными и выводятся на экран
#	
#	
#	Если запустить программу без аргументов, то производятся стандартные проверки
#       Один аргумент программа понимает как выражение и проверяет его на корректность
#	Второй аргумент — эталонный результат, c которым надо свериться

def validate_explicit(s):
  m = "#"
  for i in range(len(s)):
    m += ab2E(s[i])
    print 'm = ', unicode(m).encode('utf-8'), '\t последние пять знаков буфера: ', m[-5:]
    if m[-5:] in ["(E+E)", "(E*E)"]:
      print u'производим замену:'.encode('utf-8'), m, '\t->', m[:-5]+"E"
      m = m[:-5]+"E"
  if m == "#E":
    print u'корректное выражение'.encode('utf-8')
    return(0)
  else:
    print u'некорректное выражение'.encode('utf-8')
    return(1)

def slovami(otvet):
  if otvet == 1:
    return(u'некорректное выражение')
  elif otvet  == 0:
    return(u'корректное выражение')
  else:
    return(u'хрень какая-то')

def sxoditsja(b):
  if otvet:
    return(u'сходится') 
  else: 
    return(u'ОШИБКА') 

def test(function, test_cases):
  for tc in test_cases:
    res = function(tc[0])
    PASS = res == tc[1]
    print    otvet('\t'.join([u'проверим выражение', unicode(tc[0]), u'получается', slovami(res), u'должно быть', slovami(tc[1]), sxoditsja(PASS)]))

def main():
  if len(sys.argv) >= 2:
    expr = [(sys.argv[1], sys.argv[2])]
  else:
    expr = [("((a+b)*(a*b))",            0),
            ("a",                        0),
            ("(((a+b)+(b*b)+(a*b)))",    1),
            ("(()+(a*b))",               1),           
            ("a*b",                      1)]
  test(validate_explicit, expr)

if __name__ == '__main__':
  main()
>>>>>>> a661279e71f5edc19be2b747b2232b3c37d78d05
