# -*- coding: utf-8 -*-
"""============================================================================
Created on Tue Jan  10 15:45:27 2018
@group: Groupe 5 - Filtrage
@author: Cedric, Paul, Adrien

Main Program
============================================================================"""

from os import listdir
from Src.g5_import_json import import_daily_jsons, write_filtering_jsons
from Src.g5_integration import make_dict_filtering

"""============================================================================
    links
============================================================================"""


# LIEN SUR LE SERVEUR
# path_source = '/var/www/html/projet2018/data/clean/robot'
# path_target = '/var/www/html/projet2018/data/clean/filtering'

# LIEN SUR GITHUB
path_source = '../Data/source_press_article'
path_target = '../Data/target_press_article'

# Import Jsons
articles = import_daily_jsons(path_source)

# Treatment
dict_filtering = make_dict_filtering(articles)

# Writing
write_filtering_jsons(dict_filtering, path_target)
