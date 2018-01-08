# -*- coding: utf-8 -*-
"""============================================================================
Created on Thu Dec 21 15:52:59 2017

@author: Cedric

============================================================================"""

import os
import re
import json
from nltk.stem import SnowballStemmer

import utils.utils_filtering_v1 as utils


"""============================================================================
    links
============================================================================"""

## LIEN SUR LE SERVEUR
# path_input = '/var/www/html/projet2018/data/clean/robot
# path_target = '/var/www/html/projet2018/data/clean/filtering'


## LIEN SUR MON ORDI
file_test = 'data/jeu_test.json'
res_test = 'data/response_test.json'

#path_input = 'data/clean/robot'
#path_target = 'data/clean/filtering'

"""============================================================================
    import json
============================================================================"""

## IMPORTATIONS
with open(file_test, 'r') as dict_robot:
    articles = json.load(dict_robot)

"""============================================================================
    traitement
============================================================================"""

## Get Corpus
corpus = [articles[iart]['content'] for iart in articles]
   
## Stemmatisation
stemmer = SnowballStemmer(language = 'french',
                          ignore_stopwords = True)

stems_0 = utils.stemming(corpus[0])

## TF-IDF
df_tf_idf = utils.tf_idf(corpus)

dict_filtering = df_tf_idf.to_dict(orient='index')

"""============================================================================
    write json
============================================================================"""

with open(res_test, 'w') as outfile:
    json.dump(dict_filtering, outfile)








