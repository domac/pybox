#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

f = open("whodata.txt", "r")
for eachline in f:
    #print eachline
    #print re.split(r'\s\s+', eachline)
    print re.split(r'\s\s+|\t', eachline.strip())
f.close()