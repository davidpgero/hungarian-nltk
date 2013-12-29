#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from unittest import TestCase


class TestSnowballStemmerSentence(TestCase):
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