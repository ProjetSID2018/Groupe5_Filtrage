#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  18 15:45:27 2018
@group: Groupe 5 - Filtrage
@author: Clément BRANDAO, Maxime BRIENS, Paul LAFAURIE
"""
import numpy as np
import pickle

idf = pickle.load(
    open(
        '/var/www/html/projet2018/code/filtering/functions/lemma_idf.p',
        'rb'))
stop_words = pickle.load(
    open(
        '/var/www/html/projet2018/code/filtering/functions/stopwords.p',
        'rb'))


def tf(text_tok):
    a = [str(token) for token in text_tok]
    unique, counts = np.unique(a, return_counts=True)
    new_count = map(np.asscalar, counts)
    dict_words = dict(zip(unique, new_count))
    return dict_words


def get_tf_idf(filtered, id_article):
    dict_tf = tf(filtered)
    tfidf = []
    for key, val in dict_tf.items():
        if key not in stop_words:
            res = {
                "lemma": key,
                "tf_idf": (int(val) * idf[key]) if key in idf.keys() else 1,
                "id_hash": id_article
            }
            tfidf.append(res)
    return tfidf
