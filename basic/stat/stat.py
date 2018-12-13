#!/usr/bin/env python
#-*- coding: utf-8 -*-

import re

# 测试日志行
test_log_line = "2018-11-28 10:00:42.294 [i] [main.(*ConnscStat).PrintStats] [stat.go.85] >>> cmd [7005] allow  calls count: 207"
test_log_line2 = "2018-11-28 10:18:42.499 [i] [main.(*ConnscStat).PrintStats] [stat.go.90] >>> cmd [3164] reject calls count: 120"
test_log_line3 = "2018-11-28 10:19:42.499 [i] [main.(*ConnscStat).PrintStats] [stat.go.102] "

test_log_line4 = "2018-12-13 17:59:44.264 [i] [main.(*ConnscStat).PrintStats] [stat.go.131] +++ cmd [6003] response flow : 3491.62K"
test_log_line6 = "2018-12-13 17:57:44.264 [i] [main.(*ConnscStat).PrintStats] [stat.go.122] --- cmd [6651] request flow : 19999K"

regex = '(\d{4}[-/]\d{2}[-/]\d{2}\s+\d{2}\:\d{2}\:\d{2})\.\d+\s+\[.\]\s+\[main.\(\*ConnscStat\).PrintStats\] \[stat.go.\d+\]\s+.+\s+cmd\s+\[(\d+)\]\s+(\w+)(\s+\w+)+:\s?(\d+)'

regex2 = '(\d{4}[-/]\d{2}[-/]\d{2}\s+\d{2}\:\d{2}\:\d{2})\.\d+\s+\[.\]\s+\[main.\(\*ConnscStat\).PrintStats\] \[stat.go.\d+\]\s+.+\s+cmd\s+\[(\d+)\]\s+(\w+)(\s+\w+)+\s?:\s?(\d+)'

reg = re.compile(regex)

match1 = reg.search(test_log_line)
if hasattr(match1, 'groups'):
    print match1.groups()

match2 = reg.search(test_log_line2)
if hasattr(match2, 'groups'):
    print match2.groups()

match3 = reg.search(test_log_line3)
if hasattr(match3, 'groups'):
    print match3.groups()

reg2 = re.compile(regex2)
match4 = reg2.search(test_log_line4)
if hasattr(match4, 'groups'):
    print match4.groups()

reg2 = re.compile(regex2)
match6 = reg2.search(test_log_line2)
if hasattr(match6, 'groups'):
    print match6.groups()
