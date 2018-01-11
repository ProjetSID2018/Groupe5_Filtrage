"""============================================================================
-*- coding: utf-8 -*-
Created on Tue Jan 10 2018
@group: Groupe 5 - Filtrage
@author: Paul Lafaurie

Function : Get Part-of-Speech Tags for every word
============================================================================"""
import nltk
from nltk import ne_chunk, pos_tag
from nltk.tokenize import word_tokenize
from Src.g5_stopwords import get_stopwords

#Global variable, used many times and only needs to be loaded once
stop_words = get_stopwords()

# Goes through given POS-TAG tree if Tree not a tuple and returns a list of
# all word/tag combinations.


def getNodes(parent):
    list_node = []
    for node in parent:
        if type(node) is nltk.Tree:
            getNodes(node)
        else:
            list_node.append(node)

    return list_node


#Adds POS-Tag in a parallel list
def pos_tagging(text, stop_words = [], show=1):
    words = []
    postag = []

    # Tags Named Entities and adds POS-Tags to a tokenized text.
    for i in ne_chunk(pos_tag(word_tokenize(text))):
        if type(i) is nltk.Tree:
            # If observed token is a Tree, we have to get every token out
            # of that tree
            lst_nde = getNodes(i)
            for n in lst_nde:
                words.append(n[0])
                if (n[0] in stop_words):
                    postag.append('STOPWORD')
                else:
                    postag.append(n[1])
        else:
            # We simply add words to a list(words[]),
            # and the corresponding pos-tag to another list (postag[])
            words.append(i[0])
            if (i[0] in stop_words):
                postag.append('STOPWORD')
            else:
                postag.append(i[1])
        continue

    # Simple option to checkup on the text when the tagging is done
    if show > 0:
        print(words, '\n', postag)

    return words, postag
