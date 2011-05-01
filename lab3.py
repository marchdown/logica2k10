#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys, re, logging 
from collections import namedtuple
CFGrammar = namedtuple('Context_Free_Grammar', 'T N R S')
log = logging.getLogger("lab3")
logging.basicConfig()
log.setLevel(logging.DEBUG)
log.warn('This is a friendly warning')
log.debug('This, on the other hand, is a debug message')
########################################
####  В этом блоке задаются вспомогательные функции
####  для приведения таблиц предшествования 
####  и правил вывода в пригодный для работы вид

def parse_grammar(G, reL):
  rules = [parse_rule(r, reL) for r in G[1:-1].split('\n')]
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
######################################## Дальше разбрается таблица

def Alphabet_And_Dict_From_Precedence_Table(Precedence_Table_raw):
  hcs_raw, Precedence_Table_lines = Precedence_Table_raw.split('\n')[1], Precedence_Table_raw.split('\n')[3:] # Список строк таблицы предшествования
  L = list(l[0:1] for l in Precedence_Table_lines)         # Список символов алфавита
  reL ='['+''.join(L)+']'              # в форме, годной для регулярного выражения
  hcs = enumerate(list(hcs_raw[4::3]))            # Порядок индексов столбцов не совпадает с порядком индексов строк
  hrs = enumerate(L)                    # Нумерованный алфавит в форме итератора
  ls = list(l[3:]+' ' for l in Precedence_Table_lines)   # Строки с отрезанными головами
  return reL, dict_from_enumerated_heads_and_lines(hrs, hcs, ls)

def dict_from_enumerated_heads_and_lines(heads_rows, heads_columns,ls):
  hrs, hcs = list(heads_rows), list(heads_columns)
  logging.debug("row heads are %s, column: %s", hrs, hcs)
  d = {}
#  a = []
  for x, h in hrs:
    logging.debug("outer loop x:%s, h:%s", x, h)
    d[h] = {}
#    a[x] = []
    for y, g in hcs:
      logging.debug("inner loop y:%s, g:%s", y, g)
      d[h][g] = ls[x][3*y:3*(y+1)]
#      a[x][y] = ls[x][3*y:3*(y+1)]
  return d

########################################
#### Куски текста, которые надо разобрать

#### Третья лаба
# Правила преобразования
Expansion_Rules_raw = """
E->E+T | T
T->T*F | F
F->(E) | a
"""
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
#### Надо заметить, что пока я не вывожу N, T, S из правил, а выписываю вручную. 
T, N, S = 'a()+*', 'ETF', '#'

#### Что получается после разбора и используется в программе:
reL, PrecTable = Alphabet_And_Dict_From_Precedence_Table(Precedence_Table_raw)
R = parse_grammar(Expansion_Rules_raw, reL)
#R = parse_grammar(Expansion_Rules_raw, '['+T+N+']')
#R = [("E", "E+T"),("E", "T"),("T", "T*F"),("T", "F"),("F", "(E)"),("F", "a")]
L3 = CFGrammar(T, N, R, S)
def Prec(h, g):          #G(T) из задания. Имя T уже занято под множество конечных символов
  return PrecTable[h][g]
def tabulate(PrecTable=PrecTable): # Эта функция воспроизводит таблицу
  L = reL[1:-1]
  print '  |',
  for c in L:
    print  c+' ',
  print '\n__|' + len(L)*3*'_'
  for x in L:
    line = x + ' |'
    for y in L:
        line += Prec(x, y) #(PrecTable[x][y])
    print(line)
########################################
#### Основная логика программы
#    Программа принимает на вход выражение и проверяет его на корректность
#  с помощью таблицы предшествования
#  Выражение состоит только из конечных (основных) символов.
#
#

def prover(s_raw):
  s = s_raw+'#'
  m = '#'
  i = 0
  y = s[i]
  while y != "#":
#    log.debug('вхожу в цикл в %s-й раз из %s', i, len(s))
    x = m[-1]
    t = Prec(x, y)
    log.debug('вхожу в цикл, s = %s, m = %s, y = %s',s, m, y )
    w = True
    if ('=' in t) or ('<' in t):
      w = False
      log.debug('перенос %s на m = %s', y, m)
      m = m+y
      x = m[-1]
      i += 1
      y = s[i]
      t = Prec(x, y)
      log.debug('после переноса указатель сдвинулся на %s', y)
    if ('>' in t):
      w = False
      log.debug('свертка %s', m)
      m = recursive_sverni(m)
      x = m[-1]
    if w:
      log.debug('пусто, заканчиваем')
      return m == "#E" and y == '#'
  return m == "#E" and y == '#'

def validate(s_raw):
  log.debug( "проверяю выражение %s", s_raw)
  m = "#"
  s = s_raw+'#'
#  for y in s[::-1]:

  for i in range(len(s)):
    y = s[i]
    log.debug('[i:%s] = %s обрабатываю строку %s', i, y, s)
    x = m[-1]
    t = Prec(x,y)

    log.debug( 'сравниваю: %s на стеке и %s в строке %s', x, y, t)
    if '<' in t or '=' in t:
      m += y
      log.debug( 'в таблице есть < или =, наращиваю стек до %s', m)

    if '>' in t:
      log.warn('встретилось >, сворачиваем %s', m)
      m = '#'+ recursive_sverni(m[1:])
    log.warn( 'в таблице нет знаков. t пустое? |%s|', t)
    if ('<' not in t) and ('>' not in t) and ( '=' not in t):
      log.debug('в таблице пусто, сравниваем стек с #E')
      return m == "#E" and y == '#'
  log.debug('цикл закончен, сравниваем стек с #E')
  return m == "#E" # and y == '#'


def recursive_sverni(s):
  res = sverni(s)
  if res == s:
    log.debug( 'при последнем прогоне m остался %s, хватит сворачивать', s)

    return res # break
  log.debug('%s -> %s стек изменился, надо сворачивать заново', s, res)
  res = recursive_sverni(res)
  return res


def sverni(s):
  res = s
  for i in range(len(res)):
    log.debug( 'i = %s, сворачиваю %s', i, s[i:])
    for rule in R:
      log.debug( 'пробую правило %s', rule)
      if rule[1] == s[i:]:  # check bounds
        logging.debug( 'заменяю %s на %s',s[i:],rule[0])
        res = s[:i] + rule[0]
        break #return res
    if res != s: 
      logging.debug( 'свернуто')
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
def expand(expr, rules=R, depth=3, exprs = []):
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
