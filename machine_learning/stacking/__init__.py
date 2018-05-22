#!usr/bin/env python
# -*- coding:utf-8 -*-

"""
腾讯广告算法大赛  https://mp.weixin.qq.com/s?__biz=MzIzMzgzOTUxNA==&mid=2247483804&idx=1&sn=7f6df26aee9b29c11a6124714dbbebd5&chksm=e8fecf69df89467f7e9516f7e746075fd4918f73fc9c6f1824a4c4fae777016a91c22949a87b&scene=21#wechat_redirect
集成学习总结 & Stacking方法详解 - CSDN博客  https://blog.csdn.net/willduan1/article/details/73618677
详解stacking过程 - CSDN博客  https://blog.csdn.net/wstcjf/article/details/77989963
数据比赛大杀器----模型融合(stacking&blending) - CSDN博客  https://blog.csdn.net/u014356002/article/details/54376138
sklearn Pipeline使用 - CSDN博客  https://blog.csdn.net/SA14023053/article/details/52079542
"""

def stacking():
    from sklearn import datasets
    from sklearn import model_selection
    from sklearn.linear_model import LogisticRegression
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.naive_bayes import GaussianNB
    from sklearn.ensemble import RandomForestClassifier,GradientBoostingClassifier
    from mlxtend.classifier import StackingClassifier
    #import xgboost as xgb
    import numpy as np

    iris = datasets.load_iris()
    X, y = iris.data, iris.target

    clf1 = KNeighborsClassifier(n_neighbors=5)
    clf2 = RandomForestClassifier(random_state=1)
    clf3 = GaussianNB()
    clf4 =GradientBoostingClassifier(n_estimators=200,max_depth=6)
    lr = LogisticRegression()
    #sclf = StackingClassifier(classifiers=[clf1, clf2, clf3],meta_classifier=lr)
    sclf = StackingClassifier(classifiers=[clf1, clf2, clf3],use_probas=True,meta_classifier=lr)

    print('3-fold cross validation:\n')
    for clf, label in zip([clf1, clf2, clf3,clf4, sclf],['KNN','Random Forest','Naive Bayes',"GradientBoostingClassifier",'StackingClassifier']):
        scores = model_selection.cross_val_score(clf, X, y,cv=3, scoring='accuracy')
        print("Accuracy: %0.2f (+/- %0.2f) [%s]" % (scores.mean(), scores.std(), label))

def stacking2():
    from sklearn.datasets import load_iris
    from mlxtend.classifier import StackingClassifier
    from mlxtend.feature_selection import ColumnSelector
    from sklearn.pipeline import make_pipeline
    from sklearn.linear_model import LogisticRegression
    from sklearn import model_selection

    iris = load_iris()
    X = iris.data;y = iris.target

    pipe1 = make_pipeline(ColumnSelector(cols=(0, 2)),LogisticRegression())
    pipe2 = make_pipeline(ColumnSelector(cols=(1, 2, 3)), LogisticRegression())
    sclf = StackingClassifier(classifiers=[pipe1, pipe2],meta_classifier=LogisticRegression(),use_features_in_secondary=True
                              ,store_train_meta_features=True)
    sclf.fit(X, y)
    scores = model_selection.cross_val_score(sclf, X, y, cv=5, scoring='accuracy')
    print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std()))
    #print(sclf.train_meta_features_)

stacking()

