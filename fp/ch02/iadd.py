#!/usr/bin/env python
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    l = [1, 2, 3]

    print id(l)

    l *= 2

    #l.__iadd__(l)

    #print l

    print id(l)

    t = (1, 2, 3)

    print id(t)

    #对不可变序列进行重复拼接操作的话，效率会很低，
    #因为每次都有一个新对象，而解释器 需要把原来对象中的元素先复制到新的对象里，然后再追加新的元素。
    t *= 2

    print id(t)
