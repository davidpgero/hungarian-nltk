#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from nltk import word_tokenize


class WordTokenizeSentence:
    def __init__(self, sentence):
        self.sentence = sentence

    def tokenize_sentence(self):
        return self.__tokenize()

    def __tokenize(self):
        return word_tokenize(self.sentence)