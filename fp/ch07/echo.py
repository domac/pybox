#!/usr/bin/env python
# -*- coding: utf-8 -*-


def deco(func):
    def inner():
        print 'running inner()'

    return inner


@deco
def target():
    print 'running target()'


target()