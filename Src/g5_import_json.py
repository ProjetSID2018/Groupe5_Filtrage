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
from nltk.stem.snowball import FrenchStemmer

import utils_filtering as utils

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

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
nltk.download('stopwords')
from nltk import ne_chunk, pos_tag
from nltk.tree import Tree

# Création de la liste de stop words
stop_words = set(stopwords.words('french'))

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



#Goes through the POS-TAG tree if Tree not a tuple
def getNodes(parent):
    ROOT = 'ROOT'
    list_node = []
    for node in parent:
        if type(node) is nltk.Tree:
            getNodes(node)
        else:
            list_node.append(node)

    return list_node


#Adds POS-TAG in a parallel list
def post_ta(text, show=1):
    words = []
    postag = []
    for i in ne_chunk(pos_tag(word_tokenize(text))):
        if type(i) is nltk.Tree:
            lst_nde = getNodes(i)
            for n in lst_nde:
                words.append(n[0])
                if (n[0] in stop_words):
                    postag.append('STOPWORD')
                else:
                    postag.append(n[1])
        else:
            words.append(i[0])
            if (i[0] in stop_words):
                postag.append('STOPWORD')
            else:
                postag.append(i[1])
    if show > 0:
        print(words, '\n', postag)
    return words, postag


# Tokenisation without ponctuation
def clean_symbols(text):
    art = text.replace('?', '.')
    art = art.replace('!', '.')
    art = art.replace('…', '.')
    art = re.sub(r'[A-Za-z]’', ' ', art)
    art = re.sub(r'[A-Za-z]\'', ' ', art)
    art = re.sub(r'[^\w\s\._]', '', art, re.UNICODE)
    return art


def nltk_stemming(l_token):
    stemmer = FrenchStemmer()
    s = []
    for w in l_token:
        s.append(stemmer.stem(w))
    return s

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
        w,p = post_ta(' '.join(tokenize), show=0)
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






