#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from nltk.stem import RegexpStemmer

patterns = 'i$|t$'
regexp_stemmer = RegexpStemmer(patterns, 3)

print('With RegexpStemmer')
for word in ['Péter', 'szereti', 'Enikőt', 'és', 'Marit']:
    stem = regexp_stemmer.stem(word)
    print("Original is '{}' and stem is '{}'".format(word, stem))


