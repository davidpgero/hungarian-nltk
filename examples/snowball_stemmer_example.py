#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from nltk.stem.snowball import HungarianStemmer
from nltk import word_tokenize

stemmer = HungarianStemmer()
test_sentence = "Szeretnék kérni tőled egy óriási szívességet az édesanyám számára."

tokenized_sentence = word_tokenize(test_sentence)

for word in tokenized_sentence:
    print "Original word form is '{0}' and the root is '{1}'".format(word, stemmer.stem(word))





