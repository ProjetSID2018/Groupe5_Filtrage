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
from nltk.stem import SnowballStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize

from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

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

def get_list_of_words(text):
    # text = text.lower()
    # words_ls = re.findall('\w+', text)
    words_ls = word_tokenize(text)
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


def term_frequency(corpus, stop_words = []):
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
    countwords = CountVectorizer(tokenizer = stemming)
    countw_fit = countwords.fit_transform(corpus_ls)
    resDf = pd.DataFrame(countw_fit.A,
                         columns = countwords.get_feature_names())
    # Result
    return resDf




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
    countwords = CountVectorizer(tokenizer = stemming)
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



