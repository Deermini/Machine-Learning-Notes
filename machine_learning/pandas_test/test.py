#!usr/bin/env python
# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def cut_word(word):
    position=word.find("-")
    if position!=-1:
        bottomsalary=word[:position-1]
    else:
        bottomsalary=word[:word.upper().find("K")]
    return bottomsalary

def readcsv():
    dataframe=pd.read_csv("F:\projectfile\machine_learning\pandas_test\data\excited.csv")
    #dataframe.columns=[1,2,3,4,5]
    print(dataframe)
    print(dataframe[dataframe.salary.str.endswith("k")])
    # print("======================")
    # #print(dataframe.columns)
    # data_drop_dup=dataframe.drop_duplicates(subset="pen",keep="last")
    # print(data_drop_dup)
    # print("======================")
    # data_drop_dup['salary']=data_drop_dup.salary.apply(cut_word)
    # print(data_drop_dup.paper.describe())
    # data_drop_dup.paper.hist()
    # plt.show()
    # print(dataframe.groupby("ball").mean())

    dataframe["paper"]=dataframe["paper"].astype(str)
    print(dataframe.dtypes)

#readcsv()

def groupby_test():
    """pandas库groupby的测试"""
    data = pd.read_csv('data/groupby.csv')
    #print(data)
    gp = data.groupby('Brand')
    print(gp.count().index)
    for name, group in data.groupby(data['Brand']):
        print(name,group.Name.values)

groupby_test()




