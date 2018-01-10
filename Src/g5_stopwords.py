"""============================================================================
-*- coding: utf-8 -*-
Created on Tue Jan 10 2018
@group: Groupe 5 - Filtrage
@author: Elise Benois

Function : Get list of stop-words
============================================================================"""
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
import spacy

def get_stopwords():
    return set(stopwords.words('french'))

test = "Jean l michel a le tueur de Madame Girard"

def tokeniz(article):
    nlp = spacy.load('fr')
    doc = nlp(article)
    return doc
b = tokeniz(test)
b[2]

    
    
def rec_entity(article):

    i=0
    Ent = {}
    for entity in article.ents:
        Ent[i] = [entity.text,entity.label_]
        i +=1
    return Ent

rec_entity(b)


#list of spacy stopwords
list_stopwords = []
for find_stopwords in b:
    if find_stopwords.is_stop is True:
        list_stopwords.extend([find_stopwords])
print(list_stopwords)


