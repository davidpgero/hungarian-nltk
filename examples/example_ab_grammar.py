#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, division
from nltk import parse_cfg
from nltk import ChartParser
from random import randint

example = "ab" * randint(1, 5)

cfg = """
S -> A B
A -> 'a'
B -> 'b' || 'b' S
"""

parsed_cfg = parse_cfg(cfg)

parser = ChartParser(parsed_cfg, trace=3)

each_chars = [x for x in example]
tree = parser.parse(each_chars)

print tree

# If you'd like to see Tree, uncomment above two lines.
#from nltk.draw.tree import draw_trees
#draw_trees(tree)