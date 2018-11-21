#!/usr/bin/env python
# -*- coding: utf-8 -*-


def reverse(word):
    return word[::-1]


print reverse('domac')

fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']

print sorted(fruits)
print sorted(fruits, key=reverse)

print reverse.__doc__

print dir(reverse)

print reverse.__defaults__