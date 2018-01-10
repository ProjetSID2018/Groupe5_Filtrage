"""============================================================================
-*- coding: utf-8 -*-
Created on Tue Jan 10 2018
@group: Groupe 5 - Filtrage
@author: Paul Lafaurie

Function : Remove all non-word non-digit character
============================================================================"""

import re

"""============================================================================
    Clean Text of all weird symbols
============================================================================"""
# Tokenisation without ponctuation
#@param:text actual content of the article
def clean_symbols(text):
    #replace sentence ending punctuation by full-stop
    art = text.replace('?', '.')
    art = art.replace('!', '.')
    art = art.replace('…', '.')
    #remplace apostrophes by blanks
    art = re.sub(r'[A-Za-z]’', ' ', art)
    art = re.sub(r'[A-Za-z]\'', ' ', art)
    #remove symbols et characters other than letters and digits (accents stay)
    art = re.sub(r'[^\w\s\._]', '', art, re.UNICODE)
    #Out: text content without unecessay characters
    return art