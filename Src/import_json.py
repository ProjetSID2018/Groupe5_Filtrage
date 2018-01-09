# -*- coding: utf-8 -*-
"""============================================================================
Created on Thu Dec 21 15:52:59 2017

@author: Cedric

Par rapport à la version 1-1 :
- Importation : Adaptation a l'architecture du serveur
============================================================================"""

import os
import re
import json
from nltk.stem import SnowballStemmer
import utils_filtering as utils
from sklearn.feature_extraction.text import CountVectorizer
"""============================================================================
    links
============================================================================"""

## LIEN SUR LE SERVEUR
# path_input = '/var/www/html/projet2018/data/clean/robot
# path_target = '/var/www/html/projet2018/data/clean/filtering'

path_source = '../data/source_press_article'
path_target = '../data/target_press_article'

"""============================================================================
    import json
============================================================================"""

articles = {}

for idir in os.listdir(path_source):
    xdir = path_source + '/' + idir
    for ifile in os.listdir(xdir):
        iname = re.findall('^(.*?)_robot\.json', ifile)[0]
        
        ## IMPORT JSON :
        with open(xdir + '/' + ifile, 'r', encoding = 'utf-8') as dict_robot:
            articles[iname] = json.load(dict_robot)
            
        continue
    continue
print('End import !')

"""============================================================================
    traitement
============================================================================"""

## Get Corpus
corpus = [articles[iart]['content'] for iart in articles]

## Stemmatisation
corpus = corpus[0:5]

## TF-IDF
df_tf_idf = utils.tf_idf(corpus)
df_tf_idf.columns = list(articles)

dict_filtering = df_tf_idf.to_dict()

print('End Traitement !')

"""============================================================================
    write json
============================================================================"""

for d in dict_filtering:
    idict = dict_filtering[d]
    ifile = d + '_filtering.json'
    with open(path_target + '/' + ifile, 'w', encoding = 'utf-8') as outfile:
        json.dump(idict, outfile)

print('End writing !')






