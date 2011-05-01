#!/usr/bin/python
# -*- coding: utf-8 -*-
import logging, lab3
from lab3 import parse_rules, parse_table, CFGrammar, tabulate
log = logging.getLogger("lab4")
logging.basicConfig()
log.setLevel(logging.DEBUG)

R_raw = '''
E->E+T | T
T->T*F | F
F->(E) | N
N->N1 | N0 | 1
'''

PrecTable_raw = '''
  | E  T  F  N  0  1  (  )  +  *  #
__|________________________________ 
E |                      =  =      
T |                      >  >  =  >
F |                      >  >  >  >
N |             <= <=    >  >  >  >
0 |             >  >     >  >  >  >
1 |             >  >     >  >  >  >
) |                      >  >  >  >
( |<=  <  <  <     <  <            
+ |    <= <  <     <  <            
* |       =  <     <  <            
# | <  <  <  <     <  <            '''

reL4, PrecTable4 = parse_table(PrecTable_raw)
T, N, S = '01()+*', 'ETFN', '#'
R = parse_rules(R_raw, reL4)
L4 = CFGrammar(T, N, R, S)

def Prec(x, y):
  return lab3.Prec(x, y, pt=PrecTable4)
########################################################################
def collapse(s_raw):
  s = s_raw
  m = "#"
  a = []
  i = 0
  res = "#"
  while s[i] != '#':
    if '<' in Prec(m[-1], s[i]) or '=' in Prec(m[-1], s[i]):
      #Перенос
      m += s[i]
      i += 1
    if '>' in Prec(m[-1], s[i]):
      #Свертка
      if res != m:
        log.debug('стек %s не совпадает с %s', m, res)
        res = m
        for j in range(len(res))[i:]:
          log.debug('пробую заменить %s', m[i:])
          for rule in R:
            log.debug('пробую правило %s', rule)
            if rule[1] == m[i:]:
              log.debug('нашлось правило %s', rule)
              if rule == ('N', 'N1'):
                a[i] = 2*a[i]
              if rule == ('E', 'E+T'):
                a[i] += a[i-1]
              if rule == ('F', 'T*F'):
                a[i] *= a[i-1]
              res = m[:i] + rule[0]
            else:
              log.debug('не нашлось правила')

    if '  ' in Prec(m[-1], s[i]):
      log.debug('cell: %s', Prec(m[-1], s[i]))
      if  m == "#E":
        if  s[i] != '#':
          return False
        else: 
          return a
      
          

  

########################################
if __name__ == '__main__':
  tabulate(PrecTable4, reL4)
