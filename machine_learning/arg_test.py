#!usr/bin/env python
# -*- coding:utf-8 -*-

from tensorflow.contrib import learn
import numpy as np

max_document_length = 4
x_text =['i love you','me too']
vocab_processor = learn.preprocessing.VocabularyProcessor(max_document_length)
# vocab_processor.fit(x_text)
# print(next(vocab_processor.transform(['i me too'])).tolist())
x = np.array(list(vocab_processor.fit_transform(x_text)))
print(x)
## Extract word:id mapping from the object.
vocab_dict = vocab_processor.vocabulary_._mapping
print(vocab_dict)


