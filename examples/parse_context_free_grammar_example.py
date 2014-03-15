#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, division
import codecs
from nltk import parse_cfg
from nltk import word_tokenize
from nltk import RecursiveDescentParser


def encode(string, char_type='utf8', errors=''):
    return codecs.encode(string, char_type, errors)

cfg = encode("""
S -> NP VP NP
NP -> 'Péter' | 'Marit' | e
VP -> 'szereti' | e
""")

parsed_cfg = parse_cfg(cfg)

parser = RecursiveDescentParser(parsed_cfg)
uni_text = encode('Péter szereti Marit')
sentence = word_tokenize(uni_text)

parser = RecursiveDescentParser(parsed_cfg)
uni_text = encode('Péter szereti Marit')
sentence = word_tokenize(uni_text)

print parser.parse(sentence)