#!/usr/bin/env python
#-*- coding: utf-8 -*-

import re
import argparse
import sys

cmd = ''
op = ''
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


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', type=str, help='filepath of stat log')
    parser.add_argument('-cmd', type=str, default='', help='cmd')
    parser.add_argument('-op', type=str, default='', help='operator')
    args = parser.parse_args()
    print 'query cmd: %s, op: %s' % (args.cmd, args.op)

    if not args.f:
        print 'please input filepath using -f '
        sys.exit(1)

    cmd = args.cmd
    op = args.op
    readlines(args.f)