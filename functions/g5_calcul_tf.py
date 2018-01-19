#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 15:13:47 2018

@author: brandao
"""
import numpy as np


def tf(text_tok):
    a = [str(token) for token in text_tok]
    unique, counts = np.unique(a, return_counts=True)
    new_count = map(np.asscalar, counts)
    dict_words = dict(zip(unique, new_count))
    return dict_words
