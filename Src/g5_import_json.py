# -*- coding: utf-8 -*-
"""============================================================================
Created on Tue Jan  9 15:45:27 2018

@author: Cedric

Function : import and write json
============================================================================"""

import os
import re
import json
from tqdm import tqdm

"""============================================================================
    Functions
============================================================================"""
"""-------------------------------------
    Import Json
-------------------------------------"""
def import_daily_json(path_source):
    """
        Descr:
             Import a panel of articles according to the server structure :
                 path_source / newpaper / article
        In:
            - path_source : a string which corresponds to the localisation
        Out:
            - articles : a dict of articles

    """
    ## Initiation
    articles = {}
    newspaper_ls = os.listdir(path_source)
    ## For each inewspaper
    for inewspaper in newspaper_ls:
        xdirpaper = path_source + '/' + inewspaper
        files_ls = os.listdir(xdirpaper)
        with tqdm(desc=inewspaper, total=len(files_ls)) as fbar:
            ## Boucle : For each file
            for ifile in files_ls:
                iname = re.findall('^(.*?)_robot.json', ifile)[0]
                ## Import Json
                with open(xdirpaper + '/' + ifile, 'r', encoding = 'utf-8') as dict_robot:
                    articles[iname] = json.load(dict_robot)
                fbar.update()
                continue
    return articles


"""-------------------------------------
    Write Json
-------------------------------------"""

def write_jsons(dict_filtering, path_target):
    """
        Descr:
             write filtering jsons
        In:
            - dict_filtering : dictoinnary which contains a sub-dictionnary
                for each article.
            - path_target : a string which corresponds to the directory
                where json files must be writter
        Out :
            no result
    """
    n_art = len(dict_filtering)
    with tqdm(desc = 'Writing', total = n_art) as fbar:
        for d in dict_filtering:
            idict = dict_filtering[d]
            ifile = d + '_filtering.json'
            with open(path_target + '/' + ifile, 'w', encoding = 'utf-8') as outfile:
                json.dump(idict, outfile)
            fbar.update()
            continue
    return None
