#!/usr/bin/env python
# -*- coding: utf-8 -*-

from osconfeed import load
import collections


class FrozenJSON(object):
    def __init__(self, mapping):
        self.__data = dict(mapping)

    def __getattr__(self, name):
        if hasattr(self.__data, name):
            return getattr(self.__data, name)
        else:
            return FrozenJSON.build(self.__data[name])

    #备选构造方法
    @classmethod
    def build(cls, obj):
        if isinstance(obj, collections.Mapping):
            return cls(obj)
        elif isinstance(obj, collections.MutableSequence):
            return [cls.build(item) for item in obj]
        else:
            return obj


if __name__ == "__main__":
    raw_feed = load()
    feed = FrozenJSON(raw_feed)
    print len(feed.Schedule.keys())

    for key, value in sorted(feed.Schedule.items()):
        print('{:3} {}'.format(len(value), key))