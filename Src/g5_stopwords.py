"""============================================================================
-*- coding: utf-8 -*-
Created on Tue Jan 10 2018
@group: Groupe 5 - Filtrage
@author: Elise Benois

Function : Get list of stop-words
============================================================================"""
import nltk
import json
from nltk.corpus import stopwords
nltk.download('stopwords')
import spacy

def get_stopwords():
    return set(stopwords.words('french'))

json_data=open('/Users/Elise/Documents/Travail/M1_SID/Projet/artlmde12018-01-08_robot.json')
data = json.load(json_data)
json_data.close()

articles = {}
art = data['content']

#art = "jusqu'il Jean Michel l'abruti l tueur de Madame Girard a"

# ENLEVER LES TIRETS DANS LE TEXTE

def tokeniz(article):
   nlp = spacy.load('fr')
   doc = nlp(article)
   return doc
b = tokeniz(art)
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
type(list_stopwords[1])
list_stopwords = list(set(list_stopwords))
    print(str(list_stopwords[1]))


