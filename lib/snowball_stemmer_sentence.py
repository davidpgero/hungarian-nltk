#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from nltk.stem.snowball import HungarianStemmer
from views.snowball_stemmer_sentence_view import SnowBallStemmerSentenceView

class SnowballStemmerSentence:
    def __init__(self, tokenize_sentence, stemmer = HungarianStemmer()):
        self.sentence = tokenize_sentence
        self.stemmer = stemmer

    def pretty_result(self):
        self.__view.pretty_result

    def print_result(self):
        self.__view.print_result

    def result(self):
        return self.__stemming()

    def __view(self):
        return SnowBallStemmerSentenceView(self)

    def __stemming(self):
        return [self.__stemming_actual_word(word) for word in self.sentence]

    def __stemming_actual_word(self, word):
        return self.stemmer.stem(word)