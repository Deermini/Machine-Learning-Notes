#!usr/bin/env python
# -*- coding:utf-8 -*-

from sklearn import cluster
from sklearn.metrics import adjusted_rand_score
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets.samples_generator import make_blobs

"""
    产生数据
"""
def create_data(ncenters,num=100,std=0.7):
    X, y = make_blobs(n_samples=num, centers=ncenters, n_features=2,random_state = 0)
    return X,y

"""
    数据作图
"""
def plot_data(data):
    X,labels_true=data
    labels=np.unique(labels_true)
    fig=plt.figure()
    ax=fig.add_subplot(1,1,1)
    ax.scatter(X[:,0],X[:,1],c=labels_true)

    ax.legend(loc="best",framealpha=0.5)
    ax.set_xlabel("X[0]")
    ax.set_ylabel("Y[1]")
    ax.set_title("data")
    plt.show()


"""
    测试函数
"""
def test_AgglomerativeClustering(*data):
    X,labels_true=data
    clst=cluster.AgglomerativeClustering()
    predicted_labels=clst.fit_predict(X)
    print("ARI:%s"% adjusted_rand_score(labels_true, predicted_labels))

"""
    考察簇的数量对于聚类效果的影响
"""
def test_AgglomerativeClustering_nclusters(data):
    X,labels_true=data
    nums=range(1,50)
    ARIS=[]
    for num in nums:
        clst=cluster.AgglomerativeClustering(n_clusters=num,linkage='complete')
        predicted_lables=clst.fit(X).labels_
        print(predicted_lables)
        print(len(predicted_lables),len(set(predicted_lables)))
        ARIS.append(adjusted_rand_score(labels_true, predicted_lables))

    fig=plt.figure()
    ax=fig.add_subplot(1,1,1)
    ax.plot(nums,ARIS,marker="+")
    ax.set_xlabel("n_clusters")
    ax.set_ylabel("ARI")
    fig.suptitle("AgglomerativeClustering")
    plt.show()


centers = [(-5, -5), (0, 0), (5, 5)]
data=create_data(ncenters=centers)
plot_data(data)
test_AgglomerativeClustering_nclusters(data)