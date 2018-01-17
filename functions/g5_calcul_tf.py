#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 15:13:47 2018

@author: brandao
"""
import numpy as np


def tf(articles):
    a = []
    for i in range(len(articles)):
        a.append(str(articles[i]))
        unique, counts = np.unique(a, return_counts=True)
    dict_words = {}
    for uk, ct in zip(unique, counts):
        dict_words[uk] = int(ct)
        continue
    return dict_words
