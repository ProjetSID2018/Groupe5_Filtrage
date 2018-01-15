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
"""============================================================================
    links
============================================================================"""

# LINK ON THE SERVER
#path_source = '/var/www/html/projet2018/data/clean/robot'
#path_target = '/var/www/html/projet2018/data/clean/filtering'
#stop_words = pickle.load(open('/var/www/html/projet2018/code/filtering/functions/stopwords.p', 'rb'))

# LINK ON GITHUB
path_source = '/Users/brandao/Desktop/COURS/ProjetInterPromo-2018/Groupe5_Filtrage/Data/source_press_article'
path_target = '/Users/brandao/Desktop/COURS/ProjetInterPromo-2018/Groupe5_Filtrage/Data/target_press_article'
stop_words = pickle.load(open(
        '/Users/brandao/Desktop/COURS/ProjetInterPromo-2018/Groupe5_Filtrage/functions/stopwords.p', 'rb'))

# Import Jsons
articles = import_daily_jsons(path_source)

#sub_articles = {key : articles[key] for key in list(articles)[0:2]}

with tqdm(desc='JSONing', total=len(articles)) as pbar:
    for item in articles:
        filtered = tag_text(articles[item]['content'])
        # post = make_dict_post_filtering(item)
        ifile = path_target + '/' + item + '_filtering.json'
        with open(ifile, 'w',
                  encoding='utf-8') as outfile:
            json.dump(filtered, outfile, ensure_ascii=False)
        # write_filtering_jsons(filtered, path_target + '_filtering.json')
        pbar.update()