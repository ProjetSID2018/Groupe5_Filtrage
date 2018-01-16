"""============================================================================
-*- coding: utf-8 -*-
Created on Tue Jan 10 2018
@group: Groupe 5 - Filtrage
@author: Adrien Caminade, Paul Lafaurie and Stackoverflow, Clément BRANDAO

Function : Get named entities from text
============================================================================"""
# def get_continuous_chunks(text):
#    """
#        Summary:
#            this functions...
#        In:
#            - text:
#        Out:
#            ...
#    """
#    # Get a tree with named entities grouped together
#    chunked = ne_chunk(pos_tag(word_tokenize(text)))
#    continuous_chunk = []
#    current_chunk = []
#
#    # Parse said tree to extract in a list of strings each NE indiviually,
#    # node by node
#    for i in chunked:
#            # If current node is not a leaf
#            if type(i) == Tree:
#                # Add text from this node to the current_chunk
#                current_chunk.append(
#                        " ".join([token for token, pos in i.leaves()]))
#            # Elif current_chunk ended
#            elif current_chunk:
#                # Add current chunk to the list, reset current_chunk
#                named_entity = " ".join(current_chunk)
#                if named_entity not in continuous_chunk:
#                    continuous_chunk.append(named_entity)
#                    current_chunk = []
#            else:
#                continue
#    # Out: list of NE identified by NLTK
#    return continuous_chunk


def handing_entity(tokenize_text):  # Unique named entity version
    """
        Summary:
            this functions...
        In:
            - article:
        Out:
            ...
    """
    Ent = {}
    Ent_und = {}
    for entity in tokenize_text.ents:
        Ent[entity.text] = [entity.start_char, entity.end_char, entity.label_]
        Ent_und[entity.text.replace(" ", "_")] = entity.label_
    return Ent, Ent_und

#for ent in temp.ents:
#    print(ent.text, ent.start_char, ent.end_char, ent.label_)
#
#doc = nlp('Je m\'appelle Jean-Michel, et je vis à Paris.')
#for ent in doc.ents:
#    print(ent.text, ent.start_char, ent.end_char, ent.label_)
