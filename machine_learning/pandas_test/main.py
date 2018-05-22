#!usr/bin/env python
# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np
"医保数据的读取"
def medical():
    medical_data=pd.read_csv("F:/projectfile/yibao_yishi_data/kyry_data/kyrysfb.csv",encoding="cp936",
                             engine="python")
    #print(medical_data.get_chunk(36))
    print(medical_data.columns)
    #print(medical_data["BQZDMS"])
    # data=medical_data.get_chunk(36).ix[:,["BQZDMS"]].values
    # print(data)
    #print(set(data))

#medical()


import pandas as pd
import numpy as np

"""
Python之Pandas库学习（一）：简介 - Shadowdsp - 博客园
 http://www.cnblogs.com/fightfordream/p/7067917.html
Python之Pandas库学习（二）：数据读写 - Shadowdsp - 博客园
http://www.cnblogs.com/fightfordream/p/7071346.html
"""

def readcsv():
    dataframe=pd.DataFrame(np.arange(16).reshape(4,4),columns= ['ball', 'pen', 'pencil', 'paper'],index = ['red', 'blue', 'yellow', 'white'])
    #dataframe.to_csv("F:\projectfile\pandas_test\data\excited.csv",index=None)
    #print(dataframe)
    #print(dataframe['pencil'])
    #print(dataframe.ix[1:3,1:3])
    # dataframe.index.name="inter"
    # dataframe.columns.name="boring"
    #print(dataframe)
    #print(dataframe.corr().values)
    # print(dataframe.cov())
    #print(dataframe.pen.corr(dataframe.pencil))
    frame = pd.DataFrame([[6, np.NaN, 6], [np.NaN, 2, np.NaN], [2, np.NaN, 5]], index=['blue', 'green', 'red'],
                         columns=['ball', 'mug', 'pen'])
    #print(frame)
    #print(frame.dropna(axis=1,how="all"))
    #print(frame.fillna({"ball":1,"mug":2,"pen":3}))
    print(frame.fillna(frame.mean()))
#readcsv()

def readcsv2():
    #names=['white', 'red', 'blue', 'green', 'animal']
    dataframe = pd.read_csv("F:\projectfile\pandas_test\data\excited.csv")
    #dataframe=pd.read_csv("F:\projectfile\pandas_test\data\excited.csv",iterator=True)
    # try:
    #     df =dataframe.get_chunk(2)
    #     print(df)
    #     df = dataframe.get_chunk(2)
    #     print(df)
    # except StopIteration:
    #     print("Iteration is stopped.")

    #print(dataframe.values)
    # print(dataframe.columns)
    #dataframe["capital"]=dataframe["ball"].map({0:'zero',4:'four'})
    print(dataframe.info())
    #print(dataframe.isnull())
readcsv2()

def writecsv():
    #dataframe=pd.DataFrame(np.arange(16).reshape(4,4),columns=["red","blue","orange","black"],index=["a","b","c","d"])
    dataframe=pd.DataFrame([[1,1,np.nan],[2,np.nan,2],[np.nan,3,3]],index=[1,2,3],columns=[1,2,3])
    dataframe.to_csv("F:\projectfile\pandas_test\data\excited.csv",index=False,na_rep="nan")
    print(dataframe)
#writecsv()

def readtext():
    #dataframe=pd.read_table("F:\projectfile\pandas_test\data\excited..txt",sep="\s*")
    # dataframe = pd.read_table("F:\projectfile\pandas_test\data\excited.txt", sep="\s*",skiprows=[1,2])
    # dataframe = pd.read_table("F:\projectfile\pandas_test\data\excited.txt", sep="\s*", nrows=1)
    dataframe=pd.read_table("F:\projectfile\pandas_test\data\excited..txt",sep="\s*",chunksize=2)
    for li in dataframe:
        print(li)
#readtext()

def writerhtml():
    dataframe=pd.read_csv("F:\projectfile\pandas_test\data\excited.txt", sep="\s*")
    s = ['<HTML>']
    s.append('<HEAD><TITLE>DataFrame</TITLE></HEAD>')
    s.append('<BODY>')
    s.append(dataframe.to_html())
    s.append(dataframe.to_html())
    s.append('</BODY></HTML>')
    html = ''.join(s)
    html_file = open('F:\projectfile\pandas_test\data\dataframe.html', 'w')
    html_file.write(html)
    html_file.close()
    #print(dataframe.to_html())

#writerhtml()

def readhtml():
    #webframe=pd.read_html("F:\projectfile\pandas_test\data\dataframe.html")
    "read_html会把网页里面的所有表格都读取出来，因此需要迭代打印出来每张表格的内容"
    # for li in webframe:
    #     print(li)
    webhtml=pd.read_html("https://baike.baidu.com/item/%E5%9B%9B%E6%9C%88%E6%98%AF%E4%BD%A0%E7%9A%84%E8%B0%8E%E8%A8%80/13382872#viewPageContent")
    for li in webhtml:
        print(li)
#readhtml()


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

def readcsv5():
    dataframe=pd.read_csv("F:\projectfile\machine_learning\pandas_test\data\excited.csv")
    print(dataframe)
    print("======================")
    #print(dataframe.columns)
    data_drop_dup=dataframe.drop_duplicates(subset="pen",keep="last")
    print(data_drop_dup)
    print("======================")
    data_drop_dup['salary']=data_drop_dup.salary.apply(cut_word)
    print(data_drop_dup.paper.describe())
    data_drop_dup.paper.hist()
    plt.show()
    print(dataframe.groupby("ball").mean())

#readcsv5()


