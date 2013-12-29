#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import csv


class TSVOpener:
    def __init__(self, opt={}):
        self.name = opt.get('name')
        self.file_reader = opt.get('reader', csv)
        self.delimiter = opt.get('delimeter', b'\t')
        self.tsv = self.open_tsv_and_read_file()

    def reader(self):
        return self.tsv

    def open_tsv_and_read_file(self):
        return self.file_reader.reader(self.name, delimiter=self.delimiter)

    def build(self):
        return self.reader()

    @staticmethod
    def reader(options={}):
        return TSVOpener(options).build