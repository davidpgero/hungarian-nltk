#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from nltk.stem import RegexpStemmer


if __name__ == '__main__':
    patterns = 'i$|t$'
    regexp_stemmer = RegexpStemmer(patterns, 3)

    print('With RegexpStemmer')
    for word in ['Péter', 'szereti', 'Enikőt', 'és', 'Marit']:
        stem = regexp_stemmer.stem(word)
        print("Original word is '{}' and the stem is '{}'".format(word, stem))



