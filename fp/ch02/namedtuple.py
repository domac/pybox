#!/usr/bin/env python
# -*- coding: utf-8 -*-

import collections

if __name__ == "__main__":

    City = collections.namedtuple('City',
                                  'name country population coordinates')

    tokyo = City('Tokyo', 'JP', 37, (35.689722, 139.691667))
    print tokyo

    print hasattr(tokyo, 'population')

    print hasattr(tokyo, 'weather')

    print tokyo.population

    print tokyo._fields