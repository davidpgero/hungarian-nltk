#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, division
from nltk.tag import UnigramTagger


if __name__ == '__main__':
    model = {u'Péter': 'N', 'Enikő': 'N', 'szeret': 'V', 'Marit': 'Nacc'}
    tagger = UnigramTagger(model=model)

    print(tagger.tag(['Péter', 'Enikő', 'szeret', 'Marit']))


