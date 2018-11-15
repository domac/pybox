#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

namedRegex = r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})"

result = re.search(namedRegex, "2018-11-15")

print result.group("year")

print result.group("month")

print result.group("day")

print re.sub(namedRegex, "\g<year>/\g<month>/\g<day>", "2018-11-15")

print re.sub(r"\d+", r"[\g<0>]", "123 4 56")
