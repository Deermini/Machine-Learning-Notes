#!usr/bin/env python
# -*- coding:utf-8 -*-

"""
简单明了的LSTM/GRU应用实例（Tensorflow版） - CSDN博客  https://blog.csdn.net/baimafujinji/article/details/78279744?locationNum=3&fps=1
"""

import tensorflow as tf
import numpy as np
from tensorflow.examples.tutorials.mnist import input_data
import matplotlib.pyplot as plt

#mnist = input_data.read_data_sets('MNIST_data', one_hot=True)

mnist = input_data.read_data_sets('MNIST_data')

examples_n = 100  # display some images
indexes = np.random.choice(range(mnist.train.images.shape[0]), examples_n, replace=False)

fig = plt.figure(figsize=(5, 5))

for i in range(1, examples_n + 1):
    a = fig.add_subplot(np.sqrt(examples_n), np.sqrt(examples_n), i)
    a.axis('off')
    image = mnist.train.images[indexes[i - 1]].reshape((28, 28))
    a.imshow(image, cmap='Greys_r')

plt.show()


