#!/usr/bin/env python

"""
用python写MapReduce函数——以WordCount为例 - jihite - 博客园  https://www.cnblogs.com/kaituorensheng/p/3826114.html#_label0

运行示例：python wordcount_mapper.py < inputFile.txt | python wordcount_reducer.py
"""
import sys
def read_input(file):
    for line in file:
        yield line.split()

def main(separator='\t'):
    data = read_input(sys.stdin)
    for words in data:
        for word in words:
            print("%s%s%d" % (word, separator, 1))

if __name__ == "__main__":
    main()

