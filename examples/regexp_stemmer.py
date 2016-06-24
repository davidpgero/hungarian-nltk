#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import csv
from nltk.stem import RegexpStemmer


if __name__ == '__main__':
    patterns = 'i$|t$'
    regexp_stemmer = RegexpStemmer(patterns, 3)

    result_list = list()
    for word in ['Péter', 'szereti', 'Enikőt', 'és', 'Marit']:
        stem = regexp_stemmer.stem(word)
        result_list.append([word, stem])

    with open('output/regexp.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['word', 'stem'])
        for i in result_list:
            writer.writerow(i)

    print('See the result in output/regexp.csv')




