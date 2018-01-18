#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 15:40:40 2018

@author: brandao
"""
from functions.g5_calcul_idf import tf

idf = pickle.load(open('/Users/brandao/Desktop/COURS/ProjetInterPromo-2018/Groupe5_Filtrage/functions/lemma_idf.p', 'rb'))
idf
def get_tf_idf(tf_content_filtered, article):
    dict_tf = tf(filtered['list_lemma'])
    tfidf = []
    for key, val in dict_tf.items():
        res = {
            "lemma": key,
            "tf_idf": (int(val) * idf[key]) if key in idf.keys() else 1,
            "id_hash": article["id_art"]
            }
        tfidf.append(res)
    return tfidf
