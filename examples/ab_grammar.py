#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, division
from random import randint
from nltk import load_parser


if __name__ == '__main__':
    example = "ab" * randint(1, 5)
    parser = load_parser('file:data/ab.cfg', 3)

    each_chars = [x for x in example]
    tree = parser.parse(each_chars)

    list(tree)[0].draw()