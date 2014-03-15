#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from nltk.stem.snowball import HungarianStemmer
from nltk import word_tokenize


stemmer = HungarianStemmer()
test_sentence = "Péter szereti Enikőt és Marit"

tokenized_sentence = word_tokenize(test_sentence)

print('With SnowballStemmer')
for word in tokenized_sentence:
    print "Original word form is '{}' and the root is '{}'".format(word, stemmer.stem(word))