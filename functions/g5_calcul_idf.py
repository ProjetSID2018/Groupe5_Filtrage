#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 15:13:47 2018

@author: brandao, Tom COGNIN, Elise BENOIS
"""
import numpy as np
import math
import pickle

json_file = open('/Users/brandao/Desktop/COURS/ProjetInterPromo-2018/tf_lemma.json', encoding='utf-8')
json_data = json.load(json_file)


def tf(text_tok):
    a = [str(token) for token in text_tok]
    unique, counts = np.unique(a, return_counts=True)
    new_count = map(np.asscalar, counts)
    dict_words = dict(zip(unique, new_count))
    return dict_words


def idf(json_tf):
    dic = {}
    for article in json_data:
        for word in article:
            if word in dic.keys():
                dic[word] += 1
            else:
                dic[word] = 1

    for clé in dic:
        dic[clé] = math.log10(len(json_data)/dic[clé])
    return dic


idf = idf(json_data)
idf


fichier = open('/Users/brandao/Desktop/COURS/ProjetInterPromo-2018/Groupe5_Filtrage/functions/lemma_idf.p','wb')
pickle.dump(idf, fichier)
fichier.close()
