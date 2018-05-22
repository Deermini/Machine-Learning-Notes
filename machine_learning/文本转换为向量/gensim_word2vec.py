#!usr/bin/env python
# -*- coding:utf-8 -*-

"""
中英文维基百科语料上的Word2Vec实验 | 我爱自然语言处理
http://www.52nlp.cn/%e4%b8%ad%e8%8b%b1%e6%96%87%e7%bb%b4%e5%9f%ba%e7%99%be%e7%a7%91%e8%af%ad%e6%96%99%e4%b8%8a%e7%9a%84word2vec%e5%ae%9e%e9%aa%8c
"""
import logging
import os
import sys
import multiprocessing
import jieba
import numpy as np
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence

def load_data():
    """
    利用爬虫技术爬取一些语料
    """
    pass


def jiaba_progress():
    """
    利用jieba对已有的数据进行分词
    """
    with open('F:/github/word2vec-tensorflow/doupocangqiong.txt', "r", encoding='utf-8') as f:
        line = f.readline()
        data=open("F:/github/word2vec-tensorflow/data.txt","w")
        while line:
            while '\n' in line:
                line = line.replace('\n', '')
                line = line.replace('"', '')
            while ' ' in line:
                line = line.replace(' ', '')
            if len(line) > 0:  # 如果句子非空
                raw_words = " ".join(jieba.cut(line, cut_all=False))
                data.write(raw_words+"\n")
            line = f.readline()

def gensim_word2vec_model():
    """
    利用gensim中的word2vec模块来进行词向量的训练
    """
    inp="F:/github/word2vec-tensorflow/gensim_wor2vec/data.txt"
    model = Word2Vec(LineSentence(inp), size=400, window=5, min_count=5,
                     workers=multiprocessing.cpu_count())
    model.save("data.model")
    model.wv.save_word2vec_format("data.vector", binary=False)


"""
Gensim进阶教程：训练word2vec与doc2vec模型 - 公子天 - 博客园  https://www.cnblogs.com/iloveai/p/gensim_tutorial2.html
Gensim Word2vec 使用指南 - 简书  https://www.jianshu.com/p/52ee8c5739b6
"""
class MySentences(object):
    def __init__(self, dirname):
        self.dirname = dirname
    def __iter__(self):
        for line in open(self.dirname, encoding="utf-8"):
            yield line.split()
def gensim_word2vec_model2():
    inp = "F:/github/word2vec-tensorflow/gensim_wor2vec/data.txt"
    sentences = MySentences(inp)
    model = Word2Vec(sentences, size=400, window=5, min_count=5, workers=multiprocessing.cpu_count())
    model.save("data.model")
    model.wv.save_word2vec_format("data.vector", binary=False)


"""测试模型效果"""
def test():
    import gensim
    model = gensim.models.KeyedVectors.load_word2vec_format("data.vector", binary=False)
    content=model.most_similar("萧炎")
    for li in content:
        print(li)
    print(model["萧炎"])


def embedding():
    """如何将得到的向量文件解析传给tensorflow进行使用"""
    from tensorflow.contrib import learn

    embeddings_index = {}
    f = open(os.path.join('E:\\textm', 'glove.6B.100d.txt'),'r',encoding='utf-8')
    for line in f.readlines():
        values = line.split()
        word = values[0]
        coefs = np.asarray(values[1:], dtype='float32')
        embeddings_index[word] = coefs
    f.close()

    #############我们可以根据得到的字典生成上文所定义的词向量矩阵 https://blog.csdn.net/u013713117/article/details/69261769
    x_text = ['i love you', 'me too']
    max_document_length = max([len(x.split(" ")) for x in x_text])
    vocab_processor = learn.preprocessing.VocabularyProcessor(max_document_length)
    x = np.array(list(vocab_processor.fit_transform(x_text)))

    ## Extract word:id mapping from the object.
    word_index = vocab_processor.vocabulary_._mapping
    print(word_index)
    embedding_matrix = np.zeros((len(word_index) + 1, 100))
    for word, i in word_index.items():
        embedding_vector = embeddings_index.get(word)
        if embedding_vector is not None:
            # words not found in embedding index will be all-zeros.
            embedding_matrix[i] = embedding_vector

#jiaba_progress()
#gensim_word2vec_model()
test()


