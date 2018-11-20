#!/usr/bin/env python
# -*- coding: utf-8 -*-

import collections

if __name__ == "__main__":
    c = dict(zip(['One', 'Two', 'Three'], ['1', '2', '3']))

    print c

    d = dict(zip(('One', 'Two', 'Three'), ('1', '2', '3')))
    print d

    print d == c

    teststr = "hello"

    index = {}

    index.setdefault(teststr, []).append("world")

    print index

    index2 = collections.defaultdict(list)

    print index2

    index2["guangdong"].append("shenzhen")

    print "-------"
    for k in index2:
        print k, index2[k]

    print '-------'

    cc = collections.Counter('gsdhsaagsagfs')

    print cc
