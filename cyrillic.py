#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Foo(object):
    def __init__(self, name):
      self.name = name
      
    def __str__(self):
      return 'str: %s' % self.name
    
    def __unicode__(self):
        return 'uni: %s' % self.name.decode('utf-8')

    def __repr__(self):
      return 'repr: %s' % self.name

a = 'Елена S'
b = Foo(a)

print(str(b))
print(unicode(b))
print(repr(b))

