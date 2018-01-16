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
import numpy as np


# Server
from functions.g5_import_json import import_daily_jsons
from functions.g5_integration import tag_text
from functions.g5_database_posts import post_filtering
"""============================================================================
    links
============================================================================"""

# LINK ON THE SERVER
# path_source = '/var/www/html/projet2018/data/clean/robot'
# path_target = '/var/www/html/projet2018/data/clean/filtering'
# stop_words = pickle.load(open('/var/www/html/projet2018/code/filtering/functions/stopwords.p', 'rb'))

# LINK ON GITHUB
path_source = '/Users/brandao/Desktop/COURS/ProjetInterPromo-2018/Groupe5_Filtrage/Data/source_press_article'
path_target = '/Users/brandao/Desktop/COURS/ProjetInterPromo-2018/Groupe5_Filtrage/Data/target_press_article'
stop_words = pickle.load(open('/Users/brandao/Desktop/COURS/ProjetInterPromo-2018/Groupe5_Filtrage/functions/stopwords.p', 'rb'))

# Import Jsons
articles = import_daily_jsons(path_source)

articles = {key : articles[key] for key in list(articles)[0:5]}

log = []
test = []

with tqdm(desc='JSONing', total=len(articles)) as pbar:
    for item in articles:
        art = articles[item]
#        data_post_content = tag_text(art, f_stopwords = False, isTitle = False)
#        data_post_title = tag_text(art, f_stopwords = False, isTitle = True)
#        data_post_title = list(data_post_title)
#        for dic in range(len(data_post_title)):
#            data_post_content["position_word"].append(data_post_title[dic])
# 
#        data_post = []
#        data_post.append(data_post_content)
#        data_post = json.dumps(data_post, ensure_ascii = 'False')
#        log_post = post_filtering(data_post)
#        print(log_post)

        filtered = tag_text(art, f_stopwords = True, isTitle = False)
        art["content"] = filtered
        # post = make_dict_post_filtering(item)
        ifile = path_target + '/' + item + '_filtering.json'
        with open(ifile, 'w',
                  encoding='utf-8') as outfile:
#            json.dump(data_post_content, outfile, ensure_ascii=False)
           json.dump(art, outfile, ensure_ascii=False)
        # write_filtering_jsons(filtered, path_target + '_filtering.json')
        pbar.update()