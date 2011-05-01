#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys, re, logging 
from collections import namedtuple
CFGrammar = namedtuple('Context_Free_Grammar', 'T N R S')
log = logging.getLogger("lab3")
logging.basicConfig()
log.setLevel(logging.INFO)

########################################
####  В этом блоке задаются вспомогательные функции
####  для приведения таблиц предшествования 
####  и правил вывода в пригодный для работы вид

def parse_rules(G, reL):
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

def parse_table(Precedence_Table_raw):
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
reL, PrecTable = parse_table(Precedence_Table_raw)
R = parse_rules(Expansion_Rules_raw, reL)
#R = parse_rules(Expansion_Rules_raw, '['+T+N+']')
#R = [("E", "E+T"),("E", "T"),("T", "T*F"),("T", "F"),("F", "(E)"),("F", "a")]
L3 = CFGrammar(T, N, R, S)
def Prec(h, g, pt=PrecTable):          #G(T) из задания. Имя T уже занято под множество конечных символов
  return pt[h][g]
def tabulate(pt=PrecTable, reL=reL): # Эта функция воспроизводит таблицу
  L = reL[1:-1]
  print '  |',
  for c in L:
    print  c+' ',
  print '\n__|' + len(L)*3*'_'
  for x in L:
    line = x + ' |'
    for y in L:
        line += Prec(x, y, pt=pt) #(PrecTable[x][y])
    print(line)
########################################
#### Основная логика программы
#    Программа принимает на вход выражение и проверяет его на корректность
#  с помощью таблицы предшествования

def prover(s_raw):
  s = s_raw+'#'
  m = '#'
  i = 0
  while s[i] != "#":
    log.debug('вхожу в цикл, s = %s, m = %s, y = %s',s, m,  s[i] )
    w = True
    if ('=' in Prec(m[-1], s[i])) or ('<' in Prec(m[-1], s[i])):
      w = False
      log.info('Перенос %s на m = %s',  s[i], m)
      m += s[i]
      i += 1
      log.debug('после переноса указатель сдвинулся на %s', s[i])
    if ('>' in Prec(m[-1], s[i])):
      w = False
      log.debug('свертка %s', m)
      m = sverni(m)
    if w:
      log.debug('пусто, заканчиваем')
      return m == "#E" and  s[i] == '#'
  return m == "#E" and  s[i] == '#'

def sverni(s):
  res = b_sverni(s)
  if res == s:
    log.debug( 'при последнем прогоне m остался %s, хватит сворачивать', s)
    return res # break
  log.debug('%s -> %s стек изменился, надо сворачивать заново', s, res)
  res = sverni(res)
  return res

def b_sverni(s):
  res = s
  for i in range(len(res))[1:]:
    log.debug( 'i = %s, сворачиваю %s', i, s[i:])
    for rule in R:
      log.debug( 'пробую правило %s -> %s', rule[0], rule[1])
      if rule[1] == s[i:]:  # check bounds
        logging.debug( 'заменяю %s на %s',s[i:],rule[0])
        res = s[:i] + rule[0]
        log.info('Свертка %s -> %s', s, res)
        break #return res
    if res != s: 
      log.debug( '%s свернуто в %s', s, res)
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
