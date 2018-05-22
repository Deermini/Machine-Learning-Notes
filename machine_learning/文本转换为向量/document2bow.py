#!usr/bin/env python
# -*- coding:utf-8 -*-


def gensim_word_to_bow():
    """利用gensim库来进行转换"""
    from gensim import corpora,models,similarities

    documents = ["Shipment of gold damaged in a fire",
                 "Delivery of silver arrived in a silver truck",
                 "Shipment of gold arrived in a truck"]
    texts=[[word for word in document.lower().split()] for document in documents]
    print(texts)
    dictionary=corpora.Dictionary(texts)
    print("dictionary:",dictionary.token2id)
    corpus=[dictionary.doc2bow(text) for text in texts]
    corpus2=[dictionary.doc2idx(text) for text in texts]
    print("corpus:",corpus)
    print("corpus2:",corpus2)
    tfidf = models.TfidfModel(corpus)
    corpus_tfidf = tfidf[corpus]
    for doc in corpus_tfidf:
        print(doc)
        print("=======================")
    print("tfidf.dfs:",tfidf.dfs)


def sklearn_word_to_bow():
    """利用sklearn来进行转换"""
    from sklearn.feature_extraction.text import TfidfTransformer,CountVectorizer

    documents = ["Shipment of gold damaged in a fire",
                 "Delivery of silver arrived in a silver truck",
                 "Shipment of gold arrived in a truck"]

    # 将文本中的词语转换为词频矩阵 矩阵元素a[i][j] 表示j词在i类文本下的词频
    vectorizer = CountVectorizer()
    #fit_transform是将文本转为词频矩阵
    word_freq_matrix=vectorizer.fit_transform(documents)
    # 获取词袋模型中的所有词语
    word = vectorizer.get_feature_names()
    print("word_freq_matrix:\n",word_freq_matrix.toarray())

    # 该类会统计每个词语的tf-idf权值
    transformer = TfidfTransformer()
    # 第一个fit_transform是计算tf-idf 第二个fit_transform是将文本转为词频矩阵
    tfidf = transformer.fit_transform(word_freq_matrix)
    # 将tf-idf矩阵抽取出来，元素w[i][j]表示j词在i类文本中的tf-idf权重
    tfidf_matrix = tfidf.toarray()
    print("tfidf_matrix:\n",tfidf_matrix )

gensim_word_to_bow()



