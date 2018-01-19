"""============================================================================
-*- coding: utf-8 -*-
Created on Tue Jan 10 2018
@group: Groupe 5 - Filtrage
@author: Paul LAFAURIE, Clément BRANDAO

Function : Get Part-of-Speech Tags for every word
============================================================================"""
# import nltk
# import pickle
# from nltk import ne_chunk, pos_tag
# from nltk.tokenize import word_tokenize
import spacy
nlp = spacy.load('fr')


def tokeniz(text):  # Tokenize a text with library Spacy
    """
        Summary:
        In:
            - article: content of the article
        Out:
    """
    simple_art = text.replace("'", " ")
    doc = nlp(simple_art)
    return doc
