#!/usr/bin/env python
from operator import itemgetter
from itertools import groupby
import sys

def read_mapper_output(file, separator = '\t'):
    for line in file:
        yield line.rstrip().split(separator, 1)

def main(separator = '\t'):
    data = read_mapper_output(sys.stdin, separator = separator)
    data=sorted(data,key=lambda x:x[0])
    """ 切记：groupby前一定要先排序，要不然会失败哦"""
    for current_word, group in groupby(data, itemgetter(0)):
        try:
            total_count = sum(int(count) for current_word, count in group)
            print("%s%s%d" % (current_word, separator, total_count))
        except Exception:
            pass

if __name__ == "__main__":
    main()


