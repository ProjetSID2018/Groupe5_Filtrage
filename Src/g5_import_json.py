# -*- coding: utf-8 -*-
"""============================================================================
Created on Thu Dec 21 15:52:59 2017

@author: Cedric

Par rapport à la version 1-1 :
- Importation : Adaptation a l'architecture du serveur
============================================================================"""


import json
import g5_utils_filtering as utils

"""============================================================================
    links
============================================================================"""

## LIEN SUR LE SERVEUR
# path_input = '/var/www/html/projet2018/data/clean/robot
# path_target = '/var/www/html/projet2018/data/clean/filtering'

path_source = '../Data/source_press_article'
path_target = '../Data/target_press_article'

"""============================================================================
    import json
============================================================================"""

articles = utils.import_daily_json(path_source)

"""============================================================================
    traitement
============================================================================"""

## Get Corpus
corpus = [articles[iart]['content'] for iart in articles]

## TF-IDF
#df_freq = utils.term_frequency(corpus)
#df_freq.columns = list(articles)

#dict_filtering = df_freq.to_dict()


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



tagtext(articles["artfusc1362018-01-08"]['content'])

"""============================================================================
    write json
============================================================================"""

for d in dict_filtering:
    idict = dict_filtering[d]
    ifile = d + '_filtering.json'
    with open(path_target + '/' + ifile, 'w', encoding = 'utf-8') as outfile:
        json.dump(idict, outfile)

print('End writing !')






