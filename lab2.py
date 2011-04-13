#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
#sys.set_string_encoding("UTF-8")
def otvet(s):
  return(s.encode('utf-8'))

def validate(s):
  m = "#"
  for i in range(len(s)):
    m += ab2E(s[i])
    if m[-5:] in ["(E+E)", "(E*E)"]:
      m = m[:-5]+"E"
  if m == "#E":
      return(0)
  else:
      return(1)

def ab2E(c):
  if c in "abE":
    return 'E'
  else:
    return c
################################################################################
#	Дальше идут проверки
#	
#	Проверки устроены так: 
#	Заранее задан массив кортежей вида (выражение, корректность_выражения)
#	Все выражения по-очереди оцениваются на корректность
#       Результаты сравниваются с заданными и выводятся на экран
#	
#	
#	Если запустить программу без аргументов, то производятся стандартные проверки


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
