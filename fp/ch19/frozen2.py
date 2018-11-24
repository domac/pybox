#!/usr/bin/env python
# -*- coding: utf-8 -*-

from osconfeed import load
import collections


class FrozenJSON:
    def __new__(cls, arg):
        if isinstance(arg, collections.Mapping):
            return super().__new__(cls)
        elif isinstance(arg, collections.MutableSequence):
            return [cls(item) for item in arg]
        else:
            return arg

    def __init__(self, mapping):
        self.__data = {}
        for key, value in mapping.items():
            self.__data[key] = value

    def __getattr__(self, name):
        if hasattr(self.__data, name):
            return getattr(self.__data, name)
        else:
            return FrozenJSON(self.__data[name])


if __name__ == "__main__":
    raw_feed = load()
    feed = FrozenJSON(raw_feed)
    print len(feed.Schedule.keys())

    for key, value in sorted(feed.Schedule.items()):
        print('{:3} {}'.format(len(value), key))