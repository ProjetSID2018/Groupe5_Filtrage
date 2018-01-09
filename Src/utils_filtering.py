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
from tqdm import tqdm
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from nltk.tokenize import word_tokenize

## SKLEARN
from sklearn.feature_extraction.text import CountVectorizer

"""============================================================================
    import and write json file
============================================================================"""

def import_daily_json(daily_path):
    """
        Descr:
             Import a panel of articles according to the server structure :
                 daily_path / newpaper / article
        In:
            - daily_path : a string which corresponds to the localisation
        Out:
            - articles : a dict of articles
    """
    ## Initiation
    articles = {}
    length = len(os.listdir(daily_path))
    with tqdm(total=length) as pbar:
        for inewspaper in os.listdir(daily_path):
            xdirpaper = daily_path + '/' + inewspaper
            for ifile in os.listdir(xdirpaper):
                iname = re.findall('^(.*?)_robot\.json', ifile)[0]
                with open(xdirpaper + '/' + ifile, 'r', encoding = 'utf-8') as dict_robot:
                    articles[iname] = json.load(dict_robot)
                continue
            pbar.update()
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
    Stemming
----------------------------------------------"""

def stemming(text):
    """
        Descr:
             Stemmatisation : Analyse lexicale d'un texte
        In:
            - text (string): text to lemmatize
        Out:
            - stems : a list of words
    """
    ## adaptation of text
    text = text.lower()
    text = re.sub('\'', ' ', text)
    text = re.sub('\.\.+', ' ', text)
    ## list of words
    words_ls = word_tokenize(text)
    ## Stemmer object
    stop_words = stopwords.words('french')
    stemmer = SnowballStemmer(language = 'french')
    stems = [stemmer.stem(w) for w in words_ls if not w in stop_words]
    ## Result : list of stems words
    return stems


"""----------------------------------------------
    Term Frequency
----------------------------------------------"""

def term_frequency(corpus):
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

