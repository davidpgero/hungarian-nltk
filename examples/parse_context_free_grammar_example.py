#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from nltk import parse_cfg
from nltk import word_tokenize
from nltk import RecursiveDescentParser

cfg = """
S -> NP VP
NP -> 'Anna'
VP -> 'szeret'
"""

parsed_cfg = parse_cfg(cfg)

parser = RecursiveDescentParser(parsed_cfg)

sentence = word_tokenize('Anna szeret')

print parser.parse(sentence)