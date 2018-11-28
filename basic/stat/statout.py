#!/usr/bin/env python
#-*- coding: utf-8 -*-

import re

filepath = 'stat_full.log'
cmd = '3068'
op = 'allow'

# 正则处理
regex = '(\d{4}[-/]\d{2}[-/]\d{2}\s+\d{2}\:\d{2}\:\d{2})\.\d+\s+\[.\]\s+\[main.\(\*ConnscStat\).PrintStats\] \[stat.go.\d+\]\s+>>>\s+cmd\s+\[(\d+)\]\s+(\w+)(\s+\w+)+:\s?(\d+)'
reg = re.compile(regex)


def output(line):
    match = reg.search(line)

    if hasattr(match, 'groups'):
        groups = match.groups()
        #print groups
        if (cmd == '' or cmd == groups[1]) and (op == '' or op == groups[2]):
            print '%s %d %s %d' % (groups[0], int(groups[1]), groups[2],
                                   int(groups[4]))


def readlines(filename):
    with open(filename, 'r') as f:
        for line in f:
            output(line)


readlines(filepath)