#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, division
from nltk import load_parser
from nltk import word_tokenize


if __name__ == '__main__':
    parser = load_parser('file:data/peter_mari.cfg', 3)

    sentence = word_tokenize('Péter szereti Marit és Mari szereti Pétert')
    parsed_sentence = parser.parse(sentence)
    list(parsed_sentence)[0].draw()
