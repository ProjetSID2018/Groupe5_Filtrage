# -*- coding: utf-8 -*-
"""============================================================================
Created on Tue Jan  10 15:45:27 2018
@group: Groupe 5 - Filtrage
@author: Cedric, Paul, Adrien, Maxime

Main Program
============================================================================"""
import pickle
import json
from tqdm import tqdm


# Server
from functions.g5_import_json import import_daily_jsons
from functions.g5_integration import tag_text
from functions.g5_tf import tf
# from functions.g5_database_posts import post_filtering
"""============================================================================
    links
============================================================================"""

# LINK ON THE SERVER
path_source = '/var/www/html/projet2018/data/clean/robot'
path_target = '/var/www/html/projet2018/data/clean/filtering'
path_post_target = '/var/www/html/projet2018/data/clean/temporary_filtering'
stop_words = pickle.load(open('/var/www/html/projet2018/code/filtering/functions/stopwords.p', 'rb'))

# LINK ON GITHUB
#path_source = './Data/source_press_article'
#path_target = './Data/target_press_article'
#stop_words = pickle.load(open('./functions/stopwords.p', 'rb'))

# Import Jsons
articles = import_daily_jsons(path_source)
#articles = {key: articles[key] for key in list(articles)[0:10]}

with tqdm(desc='JSONing', total=len(articles)) as pbar:
    for item in articles:
        art = articles[item]
        data_post_content, filtered = tag_text(art, isTitle=False)
        data_post_title = tag_text(art, isTitle=True)
        data_post_title = list(data_post_title)
        for dic in range(len(data_post_title)):
            data_post_content["position_word"].append(data_post_title[dic])
        data_post = []
        data_post.append(data_post_content)
        #data_post = json.dumps(data_post, ensure_ascii='False')
        #log_post = post_filtering(data_post)
        #id_article = log_post.json()[0][0]["message"]["id_article"]
        #print('log_post = '+str(log_post)+'  |  id_article = '+str(id_article))
        ifile = path_post_target + '/' + item + '_post_filtered.json'
        with open(ifile, 'w', encoding='utf-8') as outfile:
            json.dump(data_post, outfile, ensure_ascii=False)
        
        dict_tf = tf(filtered['list_lemma'])
        tfidf = []
        for key, val in dict_tf.items():
            res = {
                "lemma": key,
                "tf_idf": int(val),
                "id_hash": art["id_art"]
                }
            tfidf.append(res)
        #log_post = post_tf(tfidf)
        ifile = path_post_target + '/' + item + '_post_tf.json'
        with open(ifile, 'w', encoding='utf-8') as outfile:
            json.dump(tfidf, outfile, ensure_ascii=False)

        art["content"] = filtered
        #art["id_article"] = id_article
        ifile = path_target + '/' + item + '_filtering.json'
        with open(ifile, 'w',
                  encoding='utf-8') as outfile:
            json.dump(art, outfile, ensure_ascii=False)
        pbar.update()
