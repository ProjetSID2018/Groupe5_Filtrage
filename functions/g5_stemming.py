"""============================================================================
-*- coding: utf-8 -*-
Created on Tue Jan 10 2018
@group: Groupe 5 - Filtrage
@author: Paul Lafaurie

Function : Get list of stemmed words from tokenized text
============================================================================"""
from nltk.stem.snowball import FrenchStemmer


def nltk_stemming(l_token):
    '''
        Summary:
            This function stems all tokens with french stemmer
            from NTLK library.
        In:
            - l_token: list of tokenized words.
        Out:
            - stems: list of stemmatized words.
    '''
    stemmer = FrenchStemmer()
    return [stemmer.stem(w) for w in l_token]
