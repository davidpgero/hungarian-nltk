#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from nltk.sem import Valuation, Model, Assignment, evaluate_sents


if __name__ == '__main__':
    valuation_describe = [
        ('ember', 'e'),
        ('asztal', 'a'),
        (['alive', set('e')]),
        (['!alive', set('a')]),
        (['agent', set('e')]),
        (['!agent', set('a')])
    ]

    valuation = Valuation(valuation_describe)
    valuation_province = Assignment(valuation.domain)
    model = Model(valuation.domain, valuation)
    sentence = 'egy asztal fut'

    res = evaluate_sents([sentence], 'file:data/semantic.fcfg', model, valuation_province)

    for i in res:
        print("The sentence: '{}'".format(sentence))
        print("The parsed tree: '{}'".format(i[0][0]))
        print("The semantic formula: '{}'".format(i[0][1]))
        print("The semantic value: '{}'".format(i[0][2]))
