"""============================================================================
-*- coding: utf-8 -*-
Created on Wed Jan 10 13:57:06 2018

@author: Cedric, Paul, Clément BRANDAO

============================================================================"""

from tqdm import tqdm
import pickle
from functions.g5_clean_text import clean_symbols
from functions.g5_POS import tokeniz
from functions.g5_named_entity import transform_entity
stop_words = pickle.load(open('/Users/brandao/Desktop/COURS/ProjetInterPromo-2018/Groupe5_Filtrage/functions/stopwords.p', 'rb'))
#stop_words = pickle.load(open('/var/www/html/projet2018/code/filtering/functions/stopwords.p', 'rb'))

"""============================================================================
    links
============================================================================"""

# LINK ON SERVER
# path_source = '/var/www/html/projet2018/data/clean/robot'
# path_target = '/var/www/html/projet2018/data/clean/filtering'

# TEST LINK
path_source = '../Data/source_press_article'
path_target = '../Data/target_press_article'

"""============================================================================
    import json
============================================================================"""
# Global variable, used many times and only needs to be loaded once
# stop_words = get_stopwords()


def analys_token(art_token, entity, entity_, with_stopwords=True):
    """
        Summary:
            This function create the dictionnary.
            Requires global variable "stop_words"
        In:
            - art_token: list of tokenized word
            - entity:
            - entity_:
            - with_stopwords: boolean:
                    * 'True' if stopwords are kept,
                    * 'False' if they are dropped.
        Out:
            - info_token : a dictionnary (length = ):
                each compartiment is a dictionnary which contains informations
                for each words
    """
    info_token = {}
    info_post = []
    words = []
    lemma = []
    i = 1
    for token in art_token:
        words.append(token.text)
        lemma.append(token.lemma_)

        if str(token.text) in stop_words:
            tag = 'STOPWORD'
        else:
            tag = token.pos_

        if str(token) in entity_.keys() and with_stopwords:
            info_token[i] = {'word': token.text,
                             'lemma': token.lemma_,
                             'pos_tag': 'Null',
                             'type_entity': entity_[str(token)],
                             'title': False}
        elif with_stopwords:
            info_token[i] = {'word': token.text,
                             'lemma': token.lemma_,
                             'pos_tag': tag,
                             'type_entity': 'Null',
                             'title': False}
        elif str(token.text) not in stop_words:
            info_post.append({'word': token.text, 'lemma': token.lemma_})
        i += 1
    if with_stopwords:
        info_token['words'] = words
        info_token['list_lemma'] = lemma
    if with_stopwords:
        return info_token
    else:
        return info_post


def tag_text(text, f_stopwords=True):
    """
        Summary:
        In:
            - article: content of the article
            /!\ il faudra a l'avenir qu'on soit rigoureux sur le nom des
            arguments : soit utiliser 'text', soit 'content', mais le meme
            de partout.
            - f_stopwords: boolean used with parameter "with_stopwords"
            from analys_token
        Out:
            2 results (see analys_tokens)
            if stopwords = True:
                a dict with:
                    - a list of all the words alongside the list of all the
                    words stems
                    - a list of of each POS-TAG (in which stop-words are tagged
                    as such regardless of what Tag they got)
           if stopwords = False:
               - a list of all the words striped of stopwords
               - a list of the word stems
    """
    # remove punctuation
    art = clean_symbols(text)
    # list of entity and list of entity here " " are replace by "_"
    entity, entity_ = transform_entity(tokeniz(art))
    for keys in entity.keys():
        art = art.replace(keys, keys.replace(" ", "_"))
    tokens = tokeniz(art)
    # Here, we decide what to return based on the bool flag f_stopwords
    if f_stopwords:
        return analys_token(tokens, entity, entity_, with_stopwords=True)
    else:
        return analys_token(tokens, entity, entity_, with_stopwords=False)


'''
def make_article_filtering(article, with_stopwords):
    """
        Summary:
            This functions...
        In:
            - article: a dictionnary structured as an article
            (see gr4 : robot)
        Out:
            - dict_filtering: dictionnary which contains articles
    """
    res_art = {}
    res_art['article'] = {
            'date_publication': article['date_publi'],
            'name_newspaper': article['newspaper'],
            'surname_author': article['author']
    }
    res_art['position_words'] = tag_text(
            article['content'],
            f_stopwords=with_stopwords
    )
    return res_art
'''

#
#def make_dict_filtering(articles):
#    """
#        Summary:
#            This functions...
#        In:
#            - articles: dictionnary which contains articles
#        Out:
#            - dict_filtering: dictionnary which contains articles
#    """
#    # initialize articles
#    dict_filtering = articles
#    n_art = len(articles)
#    with tqdm(desc='Filtering', total=n_art) as progress_bar:
#        for plain_text in articles:
#            dict_filtering[plain_text]['content'] = tag_text(
#                    articles[plain_text]['content'])
#            progress_bar.update()
#            continue
#    return dict_filtering


# def make_dict_post_filtering(articles):
#    """
#        Summary:
#            This functions...
#        In:
#            - articles: dictionnary which contains articles
#        Out:
#            - dict_filtering: dictionnary which contains articles
#    """
#    # initialize articles
#    dict_filtering = articles
#    n_art = len(articles)
#    dic = []
#    with tqdm(desc='Filtering', total=n_art) as progress_bar:
#        for plain_text in articles:
#            dict_filtering[plain_text]['content'] = tag_text(
#                    articles[plain_text]['content'], False
#                    )
#            dic.append(dict_filtering[plain_text]['content'])
#            progress_bar.update()
#            continue
#    return dic
