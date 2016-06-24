#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import csv
from nltk.stem.snowball import HungarianStemmer
from nltk import word_tokenize


if __name__ == '__main__':
    stemmer = HungarianStemmer()
    test_sentence = "Péter szereti Enikőt és Marit"

    tokenized_sentence = word_tokenize(test_sentence)

    res_list = []
    for word in tokenized_sentence:
        stem = stemmer.stem(word)
        res_list.append([word, stem])

    with open('output/snowball.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['word', 'stem'])
        for i in res_list:
            writer.writerow(i)

    print('See the result in output/snowball.csv')
