# -*- coding: utf-8 -*-
"""============================================================================
Created on Thu Dec 21 15:52:59 2017
@group: Groupe 5 - Filtrage
@author: Cedric, Paul, Adrien

Par rapport à la version 1-1 :
- Importation : Adaptation a l'architecture du serveur
============================================================================"""
import spacy

import json
from g5_import_json import import_daily_json
from g5_import_json import write_jsons

from nltk.tokenize import word_tokenize
from g5_stopwords import  get_stopwords
from g5_clean_text import clean_symbols
from g5_stemming import nltk_stemming
from g5_POS import pos_tagging
from g5_integration import tag_text, make_dict_filtering

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

articles = import_daily_json(path_source)

"""============================================================================
    traitement
============================================================================"""

## Get Corpus
corpus = [articles[iart]['content'] for iart in articles]

dict_filtering = make_dict_filtering(articles)

print('End Traitement !')


"""============================================================================
    Post tagging
============================================================================"""
from nltk.tokenize import word_tokenize
from g5_stopwords import  get_stopwords
from g5_clean_text import clean_symbols
from g5_stemming import nltk_stemming
from g5_POS import pos_tagging

# Generating  stopwords
stop_words = get_stopwords()


def tagtext(article,stpwds=True):
    #remove punctuation
    art = clean_symbols(article)

    #tokenize text
    tokenize = word_tokenize(art)
    #For parenthesis that are stuck to text
    tokenize.remove('(')
    tokenize.remove(')')
    #lemmatisation
    s = nltk_stemming(tokenize)

    if stpwds:
        w,p = pos_tagging(' '.join(tokenize), show=0)
        print(w, "\n", p,"\n",s)
        return w,p,s
    else:
        sans_stop_words = [w for w in tokenize if not w in stop_words]
        print(sans_stop_words,"\n",s)
        return sans_stop_words,s



content = tagtext(articles["artfusc1362018-01-08"]['content'])

"""============================================================================
    write json
============================================================================"""


write_jsons(dict_filtering, path_target)

print('End writing !')






