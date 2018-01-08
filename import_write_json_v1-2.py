# -*- coding: utf-8 -*-
"""============================================================================
Created on Thu Dec 21 15:52:59 2017

@author: Cedric

Par rapport à la version 1-1 :
- Importation : Adaptation a l'architecture du serveur
============================================================================"""

import os
import re
import json


"""============================================================================
    links
============================================================================"""

## LIEN SUR LE SERVEUR
# path_input = '/var/www/html/projet2018/data/clean/robot
# path_target = '/var/www/html/projet2018/data/clean/filtering'

path_source = 'data/clean/robot'
path_source += ("/" + os.listdir(path_source)[-1])

## LIEN SUR ORDI

path_target = 'data/clean/filtering'

"""============================================================================
    import json
============================================================================"""

articles = {}

for idir in os.listdir(path_source):
    xdir = path_source + '/' + idir
    for ifile in os.listdir(xdir):
        iname = re.findall('^(.*?)_robot\.json', ifile)[0]
        with open(xdir + '/' + ifile, 'r', encoding = 'utf-8') as dict_robot:
            articles[iname] = json.load(dict_robot)
        continue
    continue









