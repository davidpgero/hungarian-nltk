#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from nltk import word_tokenize

test_sentence = "Szeretnék kérni tőled egy óriási szívességet az édesanyám számára."

tokenized_sentence = word_tokenize(test_sentence)

for word in tokenized_sentence:
    print word