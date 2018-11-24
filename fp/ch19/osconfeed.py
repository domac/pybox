#!/usr/bin/env python
# -*- coding: utf-8 -*-

URL = 'http://www.oreilly.com/pub/sc/osconfeed'
JSON = 'osconfeed.json'

import json, os, warnings

import urllib


def load():

    if not os.path.exists(JSON):
        msg = 'downloading {} to {}'.format(URL, JSON)
        warnings.warn(msg)

        remote = urllib.urlopen(URL)

        with open(JSON, 'wb') as local:
            local.write(remote.read())

        remote.close()

    with open(JSON) as fp:
        return json.load(fp)


if __name__ == "__main__":

    feed = load()
    keys = sorted(feed['Schedule'].keys())

    print keys

    for key, value in sorted(feed['Schedule'].items()):
        print('{:3} {}'.format(len(value), key))
