"""============================================================================
-*- coding: utf-8 -*-
Created on Tue Jan 10 2018
@group: Groupe 5 - Filtrage
@author: Adrien Caminade, Paul Lafaurie, Clément BRANDAO

Function : Get named entities from text
============================================================================"""


def handing_entity(tokenize_text):  # Unique named entity version
    """
        Summary:
            this functions...
        In:
            - article:
        Out:
            ...
    """
    ent = {}
    ent_und = {}
    for entity in tokenize_text.ents:
        ent[entity.text] = [entity.start_char, entity.end_char, entity.label_]
        ent_und[entity.text.replace(" ", "_")] = entity.label_
    return ent, ent_und
