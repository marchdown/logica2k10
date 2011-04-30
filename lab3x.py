#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys, re
import logging 
#DEBUG = True

Expansion_Rules_raw = """
E->E+T | T
T->T*F | F
F->(E) | a
"""
########################################
####  В этом блоке разбирается текстовое представнение таблиц предшевствования и правил вывода
def parse_grammar(G=G0, reL=reL):
  rules =  [parse_rule(r, reL) for r in G[1:-1].split('\n')]
  return expand_all_rules(rules)
def parse_rule(r, reL):
  match_string = '(' + reL + '+)->(' + reL[:-1] + ' |]*)'
  match = re.search(match_string, r)
  expansion_base, expansion_results = match.group(1), match.group(2).split(' | ')
  return expansion_base, expansion_results
def expand_all_rules(rs):
  res = []
  for r in rs:
    res += expand_rule(r)
  return res
def expand_rule(r):
  res = []
  expansion_base, expansion_results = r
  for e in expansion_results:
    res.append((expansion_base, e))
  return res
G = parse_grammar(G0, reL)
#G = [("E", "E+T"),("E", "T"),("T", "T*F"),("T", "F"),("F", "(E)"),("F", "a")]
########################################
# Таблица предшествования
Precedence_Table_raw = '''
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

def Alphabet_From_Precedence_Table(Precedence_Table_raw):
  Precedence_Table_lines = Precedence_Table_raw.split('\n')[3:]
  # Список строк таблицы предшествования
  L = list(l[0:1] for l in Precedence_Table_lines)         # Список символов алфавита
  reL ='['+''.join(L)+']'              # в форме, годной для регулярного выражения
  Ln = enumerate(L)                    # Нумерованный алфавит
  Precedence_Table_data = list(l[3:]+' ' for l in Precedence_Table_lines)   # Строки с отрезанными головами

  return reL

def parsePrecTable(G):
  lines = G('\n')[3:]
  L = list(l[0:1] for l in lines)
  return (L, PrecTuples)
#G8 = ((s, r, G6[i][3*j:3*(j+1)]) for i, s in Ln for j, r in Ln)     # Кортежи вида (символ, символ, значение предшествования)
G9 = [(L[i], L[j], Precedence_Table_data[i][3*j:3*(j+1)]) for i in range(len(L)) for j in range(len(L))]
#Gdict = {(s,r):G6[i][3*j:3*(j+1)] for i, s in Ln for j, r in Ln}

def T(x, y):
  for i in range(len(G9)):
    if G9[i*9][0] == x:
      for j, r in enumerate(L):
        if y == G9[i*9 + j][1]:
          return G9[i*9 + j][2]

########################################
#### Основная логика программы

def validate(s_raw):
  logging.debug( "проверяю выражение %s", s_raw)
  m = "#"
  s = s_raw+'#'
  for i in range(len(s)):
    x = m[-1]
    y = s[i]
    t = T(x,y)
    logging.debug( 'сравниваю: %s и %s -- %s', x, y, t)
    if '<' in t or '=' in t:
      m += y
      logging.debug( 'в таблице есть <, наращиваю стек: %s+%s', m[:-1], m[-1])
    if '>' in t:
      m = '#'+ recursive_sverni(m[1:]) # there are no procedures in python
      # FIXME: check if m is changed 
      # break from for cycle
#    elif nesravnimo(x,y):
      # break from cycle
  #end cycle
    if t == '   ':
      logging.debug( 'По таблице предшествования', x, 'никогда не встечается перед',y, 'в правильном выражении')
#      if FROM_TEST: print '\n', 'несмотря на то, что это выражение было порождено с помощью тех же правил подстановки, что используются при свертке\n', 'приходится счесть его некорректным'
      break
  return m == "#E"



def recursive_sverni(s):
  res = sverni(s)
  if res == s:
    logging.debug( 'при последнем прогоне ничего не изменилось, хватит сворачивать')
    return res # break
  logging.debug( s, '->', res, 'стек изменился, надо сворачивать заново')
  res = recursive_sverni(res)
  return res


def sverni(s):
  res = s
  for i in range(len(res)):
    logging.debug( 'сворачиваю', s[-i:])
    for rule in G:
      logging.debug( 'пробую правило', rule)
      if rule[1] == s[-i:]:  # check bounds
        logging.debug( 'заменяю',s[-i:],'на',rule[0])
        res = s[:-i] + rule[0]
        break #return res
    if res != s: 
      logging.debug( 'готово дело')
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

  
################################################################################
#	Дальше идут проверки
# К счастью, для проверки достаточно породить несколько выражений
def expand(expr, rules=G, depth=3, exprs = []):
#  global.FROM_TEST = True
  if depth == 0:
    return exprs
  logging.debug( 'depth', depth)
  depth -= 1
#  res = exprs.append(expr)
  if not exprs:
    res = [expr]
  else: 
    res = exprs
  new_res = []
  for e in res:
    logging.debug( 'processing expression', e)
    for r in rules:
      logging.debug( 'trying rule', r, 'on expression', e, 'of', res)
      
      pos = e.find(r[0])
      if pos+1: 
        logging.debug( 'augmenting', e, 'with', r)
        augment = e[:pos] + r[1] + e[pos+len(r[1]):]
        if augment not in res:
          new_res.append(augment)
#        res = list(set(res))
  return expand(expr, depth=depth, exprs=new_res)
      
    
def main():
  return 0

if __name__ == '__main__':
  main()
