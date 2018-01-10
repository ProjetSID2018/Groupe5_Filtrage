# -*- coding: utf-8 -*-
"""============================================================================
Created on Wed Jan 10 13:57:06 2018

@author: Cedric

============================================================================"""

from tqdm import tqdm
import pandas as pd
from nltk.tokenize import word_tokenize
from g5_import_json import import_daily_json, write_jsons
from g5_clean_text import clean_symbols
from g5_POS import getNodes, pos_tagging
from g5_stemming import nltk_stemming
from g5_stopwords import get_stopwords

"""============================================================================
    links
============================================================================"""

## LIEN SUR LE SERVEUR
# path_source = '/var/www/html/projet2018/data/clean/robot
# path_target = '/var/www/html/projet2018/data/clean/filtering'

path_source = '../Data/source_press_article'
path_target = '../Data/target_press_article'

"""============================================================================
    import json
============================================================================"""

# articles = import_daily_json(path_source)

# text_init = articles[list(articles)[0]]['content']

def tag_text(article, stop_words = [], stpwds = True):
    #remove punctuation
    art = clean_symbols(article)
    #tokenize text
    tokenize = word_tokenize(art)
    #For parenthesis that are stuck to text
    if '(' in tokenize:
        tokenize.remove('(')
    if ')' in tokenize:
        tokenize.remove(')')
    #lemmatisation
    s = nltk_stemming(tokenize)

    if stpwds:
        w,p = pos_tagging(' '.join(tokenize), stop_words, show=0)
        return w,p,s
    else:
        sans_stop_words = [w for w in tokenize if not w in stop_words]
        return sans_stop_words,s


# words, post, stem = tag_text(text_init)


def make_dict_filtering(articles):
    # stopwords (once over all)
    stop_words = get_stopwords()
    ## initialize articles
    dict_filtering = articles
    n_art = len(articles)
    with tqdm(desc = 'Filtering', total = n_art) as fbar:
        for iart in articles:
            content = articles[iart]['content']
            words, post, stem = tag_text(content, stop_words, stpwds = True)
            dict_filtering[iart]['content'] = dict(words = words, postag = post, stem = stem)
            fbar.update()
            continue
    return dict_filtering

# dict_filtering = make_dict_filtering(articles)

# write_jsons(dict_filtering, path_target)

# make_dict_filtering()








