#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  18 15:45:27 2018
@group: Groupe 5 - Filtrage
@author: Clément, Maxime

Main Program
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


def tf(articles):
    a = []
    for i in range(len(articles)):
        a.append(str(articles[i]))
    unique, counts = np.unique(a, return_counts=True)
    dict_words = {}
    for uk, ct in zip(unique, counts):
        dict_words[uk] = ct
        continue
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
