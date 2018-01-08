# -*- coding: utf-8 -*-
"""============================================================================
Created on Wed Dec 20 09:32:45 2017

@author: Cedric Bezy

============================================================================"""


"""============================================================================
    Packages
============================================================================"""

import pandas as pd
import json
import re
from nltk.corpus import stopwords
from nltk.corpus import state_union
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, SnowballStemmer
from nltk.stem import WordNetLemmatizer

from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

"""============================================================================
    import and write json file
============================================================================"""

def import_json(file):
    """ import a json file """
    with open(file) as data:
        resjson = json.load(data)
    return resjson

def write_json(dic, file):
    """ write a json file """
    with open(file, 'w') as outfile:
        json.dump(dic, outfile)
    return None

"""============================================================================
    fonctions basiques
============================================================================"""

def Contains(pattern, x):
    """ Is a pattern contained in x string ? """
    ok = bool(re.search(str(pattern), str(x)))
    return ok

def BeginsBy(pattern, x):
    """ Does pattern begin x string ? """
    ok = Contains('^' + pattern, x)
    return ok

def EndsBy(pattern, x):
    """ Does pattern ends x string ? """
    ok = Contains(pattern + '$', x)
    return ok



"""============================================================================
    tokenize and tf_idf
============================================================================"""

def get_list_of_words(text):
    text = text.lower()
    words_ls = re.findall('\w+', text)
    return words_ls


def lemmatize(text, len_min = 3):
    """
        Descr:
             Lemmatization : Analyse lexicale d'un texte
             On cherche les différents mots.
        In:
            - text (string): text to tokenize
            - len_min = minimal length of th e words (number of character).
        Out:
            - a list of words
    """
    lemmatizer = WordNetLemmatizer()
    words_ls = get_list_of_words(text)
    lemmes = [lemmatizer.lemmatize(w) for w in words_ls]
    ## minimal length = 3 letters
    res_ls = [l for l in lemmes if len(l) >= len_min]
    return res_ls



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
    stemmer = SnowballStemmer(language = 'french', ignore_stopwords = True)
    words_ls = get_list_of_words(text)
    ## For each word
    stems = [stemmer.stem(w) for w in words_ls]
    ## minimal length = 3 letters
    res_ls = [s for s in stems if len(s) >= len_min]
    ## Result : list of words
    return res_ls


"""----------------------------------------------

----------------------------------------------"""

def tf_idf(corpus, stop_words = []):
    """
        Descr:
            From a textual corpus, return tfidf matrix for each words.
        In:
            corpus: Series(!!!) of text
            language: language for disable  stopwords
        Out:
            
    """
    corpus_ls = list(corpus)
    # trans_tf_dfs = []
    countwords = CountVectorizer(tokenizer = stemming,
                                 stop_words = stop_words)
    countw_fit = countwords.fit_transform(corpus_ls) 
    # TF-IDF
    tfidf = TfidfTransformer()
    tfidf_fit = tfidf.fit_transform(countw_fit)
    ## Matrice tf_idf
    mat_tfidf = tfidf_fit.todense().transpose()
    resDf = pd.DataFrame(mat_tfidf,
                         index = countwords.get_feature_names())
    # Result
    return resDf



