#!usr/bin/env python
# -*- coding:utf-8 -*-

from itertools import groupby
from operator import itemgetter

things = [('2009-09-02', 11),
          ('2009-09-02', 3),
          ('2009-09-03', 10),
          ('2009-09-03', 4),
          ('2009-09-03', 22),
          ('2009-09-06', 33)]

sss = groupby(things, itemgetter(0))
for key, items in sss:
    print(key)
    for subitem in items:
        print(subitem)
    print('-' * 20)