#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

teststr = "Thu Feb 15 17:46:04 2018::uzifzf@test.com::1171590364-6-8"

patt1 = '\d+-\d+-\d+'

print "1:", re.search(patt1, teststr).group()

patt2 = '.+\d+-\d+-\d+'

print "2:", re.search(patt2, teststr).group()

### + 号是一个贪婪操作符
patt3 = '.+(\d+-\d+-\d+)'
print "3:", re.search(patt3, teststr).group()
print "3:", re.search(patt3, teststr).groups()

### ？表示使用非贪婪操作
patt4 = '.+?(\d+-\d+-\d+)'
print "4:", re.search(patt4, teststr).group()
print "4:", re.search(patt4, teststr).groups()
