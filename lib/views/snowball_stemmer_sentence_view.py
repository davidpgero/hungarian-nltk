#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

class SnowBallStemmerSentenceView:

    def __init__(self, stemmer):
        self.stemmer = stemmer

    def pretty_result(self):
        for result in self.stemmer.pretty_result_msg():
            print(result)

    def print_result(self):
        print(self.result_msg())

    def pretty_result_msg(self):
        return ["{0}. '{1}'".format(key, word) for key, word in enumerate(self.stemmer.result())]

    def result_msg(self):
        return self.result()

