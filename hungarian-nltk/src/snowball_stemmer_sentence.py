#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from nltk.stem.snowball import HungarianStemmer


class SnowballStemmerSentence:
    def __init__(self, tokenize_sentence, stemmer = HungarianStemmer()):
        self.sentence = tokenize_sentence
        self.stemmer = stemmer

    def pretty_result(self):
        #for key, word in enumerate(self.result()):
        #    print "{0}. '{1}'".format(key, word)
        for result in self.pretty_result_msg():
            print result

    def pretty_result_msg(self):
        #for key, word in enumerate(self.result()):
        #    print "{0}. '{1}'".format(key, word)
        return ["{0}. '{1}'".format(key, word) for key, word in enumerate(self.result())]

    def print_result(self):
        print self.result_msg()

    def result_msg(self):
        return self.result()

    def result(self):
        return self.__stemming()

    def __stemming(self):
        return [self.__stemming_actual_word(word) for word in self.sentence]

    def __stemming_actual_word(self, word):
        return self.stemmer.stem(word)

import unittest

class TestSnowballStemmerSentence(unittest.TestCase):
    def setUp(self):
        self.test_data = ["Szeretném"]
        self.subject = SnowballStemmerSentence(self.test_data)

    def test_sentence(self):
        self.assertEqual(self.subject.sentence, self.test_data)

    def test_result(self):
        self.assertEqual(self.subject.result(), [u'szeretne'])

    def test_result_msg(self):
        self.assertEqual(self.subject.result_msg(), [u'szeretne'])

    def test_pretty_result_msg(self):
        self.assertEqual(self.subject.pretty_result_msg(), [u"0. 'szeretne'"])

if __name__ == '__main__':

    unittest.main()