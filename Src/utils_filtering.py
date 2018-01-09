# -*- coding: utf-8 -*-
"""============================================================================
Created on Wed Dec 20 09:32:45 2017

@author: Cedric Bezy

============================================================================"""


"""============================================================================
    Packages
============================================================================"""

import os
import json
import re
import pandas as pd

## NLTK
from nltk.stem import SnowballStemmer
from nltk.tokenize import word_tokenize

## SKLEARN
from sklearn.feature_extraction.text import CountVectorizer

"""============================================================================
    import and write json file
============================================================================"""

def import_daily_json(daily_path):
    articles = {}
    for idir in os.listdir(daily_path):
        xdir = daily_path + '/' + idir
        for ifile in os.listdir(xdir):
            iname = re.findall('^(.*?)_robot\.json', ifile)[0]
            with open(xdir + '/' + ifile, 'r', encoding = 'utf-8') as dict_robot:
                articles[iname] = json.load(dict_robot)
            continue
        continue
    return articles
    
"""============================================================================
    fonctions basiques
============================================================================"""

def Contains(pattern, x):
    """ Is a pattern contained in x string ? """
    ok = bool(re.search(str(pattern), str(x)))
    return ok

"""============================================================================
    tokenize and tf_idf
============================================================================"""

"""----------------------------------------------
    List of word
----------------------------------------------"""
def get_list_of_words(text):
    # text = text.lower()
    # words_ls = re.findall('\w+', text)
    words_ls = word_tokenize(text)
    return words_ls

"""----------------------------------------------
    Stemming
----------------------------------------------"""

def stemming(text, len_min = 3):
    """
        Descr:
             Stemmatisation : Analyse lexicale d'un texte
             On cherche les différents mots.
        In:
            - text (string): text to tokenize
            - len_min = minimal length of th e words (number of character).
        Out:
            - a list of words
    """
    
    ## adaptation of text
    text = text.lower()
    text = re.sub('\'', ' ', text)
    text = re.sub('\.\.+', ' ', text)
    ## list of words
    words_ls = get_list_of_words(text)
    ## Stemmer object
    stemmer = SnowballStemmer(language = 'french', ignore_stopwords = True)
    stems = [stemmer.stem(w) for w in words_ls]
    ## minimal length = 3 letters
    res_ls = [s for s in stems if len(s) >= len_min]
    ## Result : list of words
    return res_ls


"""----------------------------------------------
    Term Frequency
----------------------------------------------"""

def term_frequency(corpus, stop_words = []):
    """
        Descr:
            From a textual corpus, return term freq matrix 
            for each word in each document.
        In:
            corpus: Series(!!!) of text
            language: language for disable  stopwords
        Out:
            
    """
    corpus_ls = list(corpus)
    # trans_tf_dfs = []
    countwords = CountVectorizer(tokenizer = stemming)
    cw_fit = countwords.fit_transform(corpus_ls)
    res_freq = pd.DataFrame(cw_fit.A.transpose(),
                            index = countwords.get_feature_names())
    # Result
    return res_freq

