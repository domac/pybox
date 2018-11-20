#!/usr/bin/env python
# -*- coding: utf-8 -*-

if __name__ == "__main__":

    l = ['spam', 'spam', 'eggs', 'eggs']

    z = ['spam']

    print list(set(l))
    print list(set(l).intersection(set(z)))
