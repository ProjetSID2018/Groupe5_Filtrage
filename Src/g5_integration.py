"""============================================================================
-*- coding: utf-8 -*-
Created on Wed Jan 10 13:57:06 2018

@author: Cedric, Paul, Clément BRANDAO

============================================================================"""

from tqdm import tqdm
from Src.g5_clean_text import clean_symbols
from Src.g5_POS import pos_tagging, tokeniz, analys_token
from Src.g5_stemming import nltk_stemming
from Src.g5_stopwords import get_stopwords
from Src.g5_named_entity import recognize_entity

"""============================================================================
    links
============================================================================"""

# LINK ON SERVER
# path_source = '/var/www/html/projet2018/data/clean/robot
# path_target = '/var/www/html/projet2018/data/clean/filtering'

path_source = '../Data/source_press_article'
path_target = '../Data/target_press_article'

"""============================================================================
    import json
============================================================================"""
# Global variable, used many times and only needs to be loaded once
stop_words = get_stopwords()


def tag_text(article, f_stopwords=True):
    # remove punctuation
    art = clean_symbols(article)
    # tokenize text
    tokenize = tokeniz(art)
    
    # Return list of entity end list of entity here " " are replace by "_"
    entity, entity_ = recognize_entity(tokenize)
    for keys in entity.keys():
        art = article.replace(keys, keys.replace(" ", "_"))
    tokenize = tokeniz(art)

    # Here, we decide what to return based on the bool flag f_stopwords
    # if f_stopwords is True, we return the list of all the words alongside the
    # list of all the word stems and
    # a list of each POS-TAG (in which stop-words are tagged as such regardless
    # of what Tag they got)
    # if f_stopwords is False, we return a list of all the words striped of
    # stopwords, and the word stems
    if f_stopwords:
        return analys_token(tokenize, entity, entity_)
    else:
        return analys_token(tokenize, entity, entity_, False)


def make_dict_filtering(articles):
    # initialize articles
    dict_filtering = articles
    n_art = len(articles)
    with tqdm(desc='Filtering', total=n_art) as progress_bar:
        for plain_text in articles:
            dict_filtering[plain_text]['content'] = tag_text(articles[plain_text]['content'])
            progress_bar.update()
            continue
    return dict_filtering
