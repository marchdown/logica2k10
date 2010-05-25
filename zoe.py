#!/usr/bin/python -tt
"""Another take at partitio numerorum problem
"""
import os
import sys
import re
A = ['1', '+', '=']

def ep_helper(given):
  result = []
  for s in given:
    for a in A:
      result.append(s + a)
  return result 
    
def ep_main(maxlen):
  res = []
  for i in range(maxlen):
    ep_helper(res)

def enum_possible(maxlength):
  grad = [['']]

  if maxlength >= 0:
    for i in range(maxlength):
      grad.append([])
      for a in A:
        for s in grad[i]:
          grad[i+1].append(s+a)
  return grad
def fmt_ep(g):
  for l in g:
    print len(l)
#    if len(l) < 10
        
def divisors(n):
  res = []
  for i in range(n//2):
    if n % (i+1) == 0:
      res.append(i+1)
  return res
  
def enum_correct_strict(l):
  if l < 1:
    print "no strings shorter than '='"
    return []
  if l == 1:
    return ['=']
  # generate strings without '+'s first
#  for i in range(l//2))
  clean_list = []
  for i in divisors(l+1)[1:]:
    len_link = (l+1)/i
    link = '1'*(len_link-1)+'='
    s = (link*i)[:-1]
    #((('1'*(n/i - 1))+'=')*i)[:-1]
    clean_list.append(s)
  return clean_list     

# def enum_correct_upto(l):
#   result = []
#   for i in range(l-1):
#     shorter_strings = enum_correct_strict(i+1)
#     for s in shorter_strings:
#       for cut_index in range(len(s)):
#         aug_s = s[:cut_index] + '+' + s[cut_index:] 

def augment_once(s):
  result = []
  for cut_index in range(len(s)):
        #s = s[:cut_index] + '+' + s[cut_index:]
      (pref, suf) = s[:cut_index], s[cut_index:]
      aug_s = '+'.join([pref, suf])
      if not aug_s in result:
        result.append(aug_s)
  return result
  
def augment_string(s, l):
  result = []
  for j in range(l-len(s)):
      auglist = augment_once(s)
      for augstr in auglist:
          aug2list = augment_string(augstr, l)    
          result.extend(aug2list)
  return result    
# result.append(s)
def cut_into_groups(uncut_str):
  result = ['']
  for i in range(len(uncut_str)):
    result.append( uncut_str[i])
  return result

def aug_gl(g, upto):
  print 'entering the agu_gl with %r and going up to %d' % (g, upto)
  result = []
  wlist = [g]
  maxindex = (len(g))
  numsteps = upto - (len(g) -1)
  print 'I will have to add +s in %d steps, filling from zero to %d numbered cuts on each' % (numsteps, maxindex)
  for j in range(numsteps):
    wlist.append([])
    print 'extending %r' % wlist
    for i in range(maxindex):
      wlist[j+1].append(wlist[j][i]+ '+')
      print 'wlist is now %r' % wlist
  for j in len(wlist):
    for i in len(j):
      result.append(''.join(i))
  return result

def enum_correct_upto(l): 
  shorter_correct_strings = []
  augmented_strings = []
  for i in range(l-1):  # generate all correct strings of lengths < l
    temp = enum_correct_strict(i+1)
    if temp:
      shorter_correct_strings.extend(temp)
  for s in shorter_correct_strings: #bring each of them to length l
    print s, 'bringing s up to the proper length'
    cut_str = cut_into_groups(s)
    print cut_str, 'cut it by character, adding empy string at the head'
    augmented_cut_strs = aug_gl(cut_str, upto=l) 
    print augmented_cut_strs, 'brought it up to length'
    augmented_strings.extend(augmented_cut_strs)
  return enum_correct_strict(l) + augmented_strings


argv = sys.argv[1:]
l = 11
if argv:
#  if c in argv:
  l = argv[0]
    
def print_enum(l):
  default_length = l
#  s = enum_correct_upto(default_length)
  s = enum_correct_strict(default_length)
  print '%r divide %d' % (divisors(default_length), default_length)
  print 'there are %d correct strings of length %d' % (len(s), default_length)
  for i in s:
    print i
  print

  augs = enum_correct_upto(default_length)
  print '%d augmented strings: ' % len(augs)
  print augs
    

  
def main():
  print_enum(l)
  sys.exit(0)
if __name__ == '__main__':
  main()



## version control ftw!
