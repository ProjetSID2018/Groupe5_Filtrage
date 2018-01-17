# -*- coding: utf-8 -*-
"""============================================================================
Created on Tue Jan  10 15:45:27 2018
@group: Groupe 5 - Filtrage
@author: Cedric, Paul, Adrien, Maxime

Main Program
============================================================================"""
import numpy as np

def tf(articles):
   a = []
   for i in range(len(articles)):
       a.append(str(articles[i]))
   unique, counts = np.unique(a, return_counts=True)
   dict_words = {}
   for uk, ct in zip(unique, counts):
       dict_words[uk] = ct
       continue
   return dict_words