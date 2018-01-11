"""============================================================================
-*- coding: utf-8 -*-
Created on Tue Jan 10 2018
@group: Groupe 5 - Filtrage
@author: Adrien Caminade, Paul Lafaurie and Stackoverflow

Function : Get named entities from text
============================================================================"""
from nltk import ne_chunk, pos_tag
from nltk.tree import Tree
from nltk.tokenize import word_tokenize

import spacy
nlp = spacy.load('fr_core_news_sm')
doc = nlp(u"C'est une phrase.")
print([(w.text, w.pos_) for w in doc])

#Returns named entities identified by nltk in the @param:text
#Copy/Pasted from Stackoverflow (not used for now)
def get_continuous_chunks(text):
    #get a tree with named entities grouped together
    chunked = ne_chunk(pos_tag(word_tokenize(text)))
    continuous_chunk = []
    current_chunk = []
    #parse said tree to extract in a list of strings each NE indiviually, node by node
    for i in chunked:
            #if current node is not a leaf
            if type(i) == Tree:
                    #add text from this node to the current_chunk
                    current_chunk.append(" ".join([token for token, pos in i.leaves()]))
            #elif current_chunk ended
            elif current_chunk:
                #add current chunk to the list, reset current_chunk
                named_entity = " ".join(current_chunk)
                if named_entity not in continuous_chunk:
                    continuous_chunk.append(named_entity)
                    current_chunk = []
            else:
                continue
    #out: list of NE identified by NLTK
    return continuous_chunk