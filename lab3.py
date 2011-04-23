#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys, re
DEBUG = True

# G0 = """
# E->E+T | T
# T->T*F | F
# F->(E) | a
# """

G = [("E", "E+T"),("E", "T"),("T", "T*F"),("T", "F"),("F", "(E)"),("F", "a")]

def validate(s_raw):
  if DEBUG: print 'проверяю выражение', s_raw
  m = "#"
  s = s_raw+'#'
  for i in range(len(s)):
    x = m[-1]
    y = s[i]
    t = T(x,y)
    if DEBUG: print 'сравниваю: ', x, 'и',y, '—', t
    if '<' in t or '=' in t:
      m += y
      if DEBUG: print 'в таблице есть <, наращиваю стек:', m[:-1], '->', m
    if '>' in t:
      m = '#'+ recursive_sverni(m[1:]) # there are no procedures in python
      # FIXME: check if m is changed 
      # break from for cycle
#    elif nesravnimo(x,y):
      # break from cycle
  #end cycle
    if t == '   ':
      if DEBUG: print 'По таблице предшествования', x, 'никогда не встечается перед',y, 'в правильном выражении'
      if FROM_TEST: print '\n', 'несмотря на то, что это выражение было порождено с помощью тех же правил подстановки, что используются при свертке\n', 'приходится счесть его некорректным'
      break
  return m == "#E"



def recursive_sverni(s):
  res = sverni(s)
  if res == s:
    if DEBUG: print 'при последнем прогоне ничего не изменилось, хватит сворачивать'
    return res # break
  if DEBUG: print s, '->', res, 'стек изменился, надо сворачивать заново'
  res = recursive_sverni(res)
  return res


def sverni(s):
  res = s
  for i in range(len(res)):
    if DEBUG: print 'сворачиваю', s[-i:]
    for rule in G:
      if DEBUG: print 'пробую правило', rule
      if rule[1] == s[-i:]:  # check bounds
        if DEBUG: print 'заменяю',s[-i:],'на',rule[0]
        res = s[:-i] + rule[0]
        break #return res
    if res != s: 
      if DEBUG: print 'готово дело'
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

# Таблица предшествования
G4 = '''
  | E  T  F  a  (  )  +  *  #
__|__________________________
E |                =  =      
T |                >  >  =  >
F |                >  >  >  >
a |                >  >  >  >
) |                >  >  >  >
( |<=  <  <  <  <            
+ |    <= <  <  <            
* |       =  <  <            
# | <  <  <  <  <            '''

G5 = G4.split('\n')[3:]              # Список строк таблицы предшествования
L = list(l[0:1] for l in G5)         # Алфавит
Ln = enumerate(L)                    # Нумерованный алфавил
G6 = list(l[3:]+' ' for l in G5)     # Строки с отрезанными головами

def parsePrecTable(G):
  lines = G('\n')[3:]
  L = list(l[0:1] for l in lines
  return (L, PrecTuples)
#G8 = ((s, r, G6[i][3*j:3*(j+1)]) for i, s in Ln for j, r in Ln)     # Кортежи вида (символ, символ, значение предшествования)
G9 = [(L[i], L[j], G6[i][3*j:3*(j+1)]) for i in range(9) for j in range(9)]
#Gdict = {(s,r):G6[i][3*j:3*(j+1)] for i, s in Ln for j, r in Ln}
def T(x, y):
  for i in range(len(G9)):
    if G9[i*9][0] == x:
      for j, r in enumerate(L):
        if y == G9[i*9 + j][1]:
          return G9[i*9 + j][2]
  
################################################################################
#	Дальше идут проверки
# К счастью, для проверки достаточно породить несколько выражений
def expand(expr, rules=G, depth=3, exprs = []):
  global.FROM_TEST = True
  if depth == 0:
    return exprs
  if DEBUG: print 'depth', depth
  depth -= 1
#  res = exprs.append(expr)
  if not exprs:
    res = [expr]
  else: 
    res = exprs
  new_res = []
  for e in res:
    if DEBUG: print 'processing expression', e
    for r in rules:
      if DEBUG: print 'trying rule', r, 'on expression', e, 'of', res
      
      pos = e.find(r[0])
      if pos+1: 
        if DEBUG: print 'augmenting', e, 'with', r
        augment = e[:pos] + r[1] + e[pos+len(r[1]):]
        if augment not in res:
          new_res.append(augment)
#        res = list(set(res))
  return expand(expr, depth=depth, exprs=new_res)
      
    
def main():
  return 0

if __name__ == '__main__':
  main()
