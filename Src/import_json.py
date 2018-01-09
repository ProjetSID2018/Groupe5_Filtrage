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
from sklearn.feature_extraction.text import CountVectorizer

import utils_filtering as utils

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

articles = utils.import_daily_json(path_source)

"""============================================================================
    traitement
============================================================================"""

## Get Corpus
corpus = [articles[iart]['content'] for iart in articles]

## TF-IDF
df_freq = utils.term_frequency(corpus)
df_freq.columns = list(articles)

dict_filtering = df_freq.to_dict()


print('End Traitement !')


"""============================================================================
    Post tagging
============================================================================"""

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
nltk.download('stopwords')
from nltk import ne_chunk, pos_tag
from nltk.tree import Tree

example_sentence = "bonjour, tous le monde vas bien? J'espere que oui."

 # Création de la liste de stop words
stop_words = set(stopwords.words('french'))

 # Tokenisation sans ponctuation
tokenize_avec_ponctu = word_tokenize(example_sentence)
tokenize= [w for w in tokenize_avec_ponctu if not w in [',','?',';','.',':','!','+','*','>','<','&','~','#','{','}','(',')','[',']','|','°','=','$','£','¤','%','µ','§']]

 # Supprime les stops words
sans_stop_words = [w for w in tokenize if not w in stop_words]

 # Permet le post tagging
 # Chunk permet d'avoir les entitées nommée.
def get_continuous_chunks(text): # code pris sur stack overflow (améliorable)
     chunked = ne_chunk(pos_tag(word_tokenize(text)))
     prev = None
     continuous_chunk = []
     current_chunk = []
     for i in chunked:
             if type(i) == Tree:
                     current_chunk.append(" ".join([token for token, pos in i.leaves()]))
             elif current_chunk:
                     named_entity = " ".join(current_chunk)
                     if named_entity not in continuous_chunk:
                             continuous_chunk.append(named_entity)
                             current_chunk = []
             else:
                     continue
     return continuous_chunk
 
def post_ta(text,show=1):  
    words=[]
    postag=[]
    for i in ne_chunk(pos_tag(word_tokenize(text))): 
        words.append(i[0])
        postag.append(i[1])
    if show >0:
        print(words,'\n',postag)
    return words,postag

post_ta(' '.join(sans_stop_words),show=0)

"""============================================================================
    write json
============================================================================"""

for d in dict_filtering:
    idict = dict_filtering[d]
    ifile = d + '_filtering.json'
    with open(path_target + '/' + ifile, 'w', encoding = 'utf-8') as outfile:
        json.dump(idict, outfile)

print('End writing !')






