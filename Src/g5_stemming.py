"""============================================================================
-*- coding: utf-8 -*-
Created on Tue Jan 10 2018
@group: Groupe 5 - Filtrage
@author: Paul Lafaurie

Function : Get list of stemmed words from tokenized text
============================================================================"""
from nltk.stem.snowball import FrenchStemmer

def nltk_stemming(l_token):
    stemmer = FrenchStemmer()
    s = []
    for w in l_token:
        s.append(stemmer.stem(w))
    return s