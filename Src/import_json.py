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
from nltk.stem import SnowballStemmer
from sklearn.feature_extraction.text import CountVectorizer

import utils_filtering as utils

"""============================================================================
    links
============================================================================"""

## LIEN SUR LE SERVEUR
# path_input = '/var/www/html/projet2018/data/clean/robot
# path_target = '/var/www/html/projet2018/data/clean/filtering'

path_source = '../data/source_press_article'
path_target = '../data/target_press_article'

"""============================================================================
    import json
============================================================================"""

articles = utils.import_daily_json(path_source)

"""============================================================================
    traitement
============================================================================"""

## Get Corpus
corpus = [articles[iart]['content'] for iart in articles]

## TF-IDF
df_freq = utils.term_frequency(corpus)
df_freq.columns = list(articles)

dict_filtering = df_freq.to_dict()


print('End Traitement !')


"""============================================================================
    Post tagging
============================================================================"""

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
nltk.download('stopwords')
from nltk import ne_chunk, pos_tag
from nltk.tree import Tree

example_sentence = "La  police  britannique a révélé, mardi 6 juin, l’identité du dernier des trois assaillants qui ont semé la terreur sur le London Bridge et à Borough Market à Londres samedi. L’attentat a fait sept morts, dont une Canadienne, une Australienne et un Français, et quarante-huit blessés. Les trois terroristes tués par la police s’appelaient Khuram Shazad Butt, Rachid Redouane et Youssef Zaghba. Les deux premiers vivaient dans le quartier multiculturel de Barking, dans l’est de Londres, où la police a arrêté plusieurs personnes ces derniers jours. Khuram Shazad Butt, 27 ans Citoyen britannique, né le 20 avril 1990 au  Pakistan , Khuram Shazad Butt était connu des services de sécurité. Il avait fait l’objet d’une  enquête  des services britanniques et sa radicalisation avait été signalée à plusieurs reprises aux services de renseignement. Ces derniers n’avaient toutefois pas d’éléments laissant  penser  qu’il préparait un attentat, a déclaré le commandant de l’unité antiterroriste de Londres, Mark Rowley. Khuram Shazad Butt, père de deux jeunes enfants, dont un nouveau-né de quelques semaines, avait travaillé comme apprenti au service clients du métro de Londres pendant six mois l’année dernière. Depuis, il travaillait quelques heures par semaine dans un  centre  de  sport  islamique, où il pratiquait notamment la  boxe  et le taekwondo, selon  The Times . \n        Lire notre synthèse:\n         \n     \n          Attentat de Londres : la police dévoile l’identité de deux des trois assaillants\n           \n Selon plusieurs  médias  britanniques, le Londonien regardait régulièrement des  vidéos  de prêches d’Ahmad Musa Jibril, connu pour leur violence extrême. En 2016, Khuram Shazad Butt s’était fait  remarquer  dans un documentaire de la chaîne Channel 4 intitulé  The Jihadis Next Door  (« mes voisins les djihadistes »), consacré aux djihadistes britanniques .  Il y apparaissait au côté de prêcheurs radicaux, déployant un drapeau de l’organisation  Etat islamique  dans Regent’s Park, à Londres, et se livrant à une prière dans sa tunique pakistanaise traditionnelle. A l’issue de cette scène, Khuram Shazad Butt et les hommes qui l’accompagnaient avaient été retenus par la police, qui faute d’avoir retrouvé le drapeau les avait libérés une heure plus tard. Selon le  Guardian , cette scène était typique du  mode  opératoire d’Al-Muhajiroun, un groupe désormais interdit d’agitateurs islamistes ancré dans l’est de Londres, et dont Khuram Shazad Butt était un partisan. Son leader, le prédicateur Anjem Choudary, est resté très actif, même après l’attentat de Londres de 2005, qui avait conduit à la dissolution du groupe. Le meneur avait finalement été condamné en 2016 à cinq ans de prison pour  avoir  fait l’apologie de l’Etat islamique. Plusieurs habitants de la barre d’immeuble de Barking où il vivait ont témoigné que Khuram Shazad Butt était connu pour  parler  de religion aux adolescents du quartier, voire de  faire  du prosélytisme auprès d’enfants à grands renforts de bonbons et chocolats. En mai 2013, alors que deux islamistes venaient d’égorger le militaire britannique Lee Rigby à Londres, Khuram Shazad Butt s’était rendu devant le Parlement, où se tenait un rassemblement en hommage à la victime, y multipliant les provocations.  « Il m’a traité de “murtad”, ce qui signifie “traître” en arabe, et il m’a accusé de  travailler  pour le gouvernement »,  se rappelle Mohammed Shafiq, le fondateur de la Ramadhan Foundation, une association de jeunes musulmans de Manchester, présent ce jour-là. Khuram Shazad Butt avait été vu il y a quelques semaines dans l’est de Londres enjoignant aux électeurs de ne pas  participer  aux élections du 8 juin. Il était fan du club de  football  d’Arsenal, dont il portait le maillot samedi soir au moment de l’attentat. \n        Lire aussi :\n         \n     \n                Sous la pluie, l’hommage de Londres aux victimes de l’attentat\n     \n Rachid Redouane, 30 ans Le second assaillant, Rachid Redouane, était lui inconnu des services de renseignement. Né le 31 juillet 1986, l’homme disait  être  de nationalités marocaine et libyenne. Il utilisait aussi l’identité de Rachid Elkhdar, avec une date de naissance différente, le 31 juillet 1991. Selon la chaîne de télévision publique irlandaise  RTE , citant des sources policières, il serait de nationalité marocaine et aurait résidé en  Irlande . Il était marié à une Ecossaise. \n        Lire aussi :\n         \n     \n                Attentat de Londres : comment Aamaq est devenue l’« agence attentats » de l’EI\n     \n Selon RTE, un document retrouvé sur le corps de l’un des assaillants a mis les enquêteurs sur la piste irlandaise. Il s’agit, disent des sources policières, d’une autorisation de séjour de plus de trois mois pour ressortissant d’un pays n’appartenant pas à l’ Union européenne . Youssef Zaghba, 22 ans Youssef Zaghba, présenté comme  le  « fils d’une femme de Bologne »   par le quotidien italien  La Reppublica , est le troisième et dernier homme à avoir été formellement identifié comme l’un des auteurs de l’attentat, mardi 6 juin. Agé de 22 ans, il serait d’origine italiano-marocaine. Scotland Yard dit qu’il n’était pas dans le radar des autorités. Mais selon les quotidiens italiens  Corriere della Sera  et  La Repubblica , il avait été en revanche repéré et signalé par le renseignement italien, notamment après une tentative de départ en  Syrie ."


 # Création de la liste de stop words
stop_words = set(stopwords.words('french'))

 # Tokenisation sans ponctuation
tokenize_avec_ponctu = word_tokenize(example_sentence)
tokenize= [w for w in tokenize_avec_ponctu if not w in ['“','”','«','»',',','?',';','.',':','!','+','*','>','<','&','~','#','{','}','(',')','[',']','|','°','=','$','£','¤','%','µ','§','’']]

 # Supprime les stops words
sans_stop_words = [w for w in tokenize if not w in stop_words]

 # Permet le post tagging
 # Chunk permet d'avoir les entitées nommée.
def get_continuous_chunks(text): # code pris sur stack overflow (améliorable)
     chunked = ne_chunk(pos_tag(word_tokenize(text)))
     prev = None
     continuous_chunk = []
     current_chunk = []
     for i in chunked:
             if type(i) == Tree:
                     current_chunk.append(" ".join([token for token, pos in i.leaves()]))
             elif current_chunk:
                     named_entity = " ".join(current_chunk)
                     if named_entity not in continuous_chunk:
                             continuous_chunk.append(named_entity)
                             current_chunk = []
             else:
                     continue
     return continuous_chunk
 
 # getNode permet de séparer en tuple
def getNodes(parent):
    ROOT = 'ROOT'
    list_node = []
    for node in parent:
        if type(node) is nltk.Tree:
            if node.label() == ROOT:
                print ("======== Sentence =========")
                print ("Sentence:", " ".join(node.leaves()))
            else:
                print ("Label:", node.label())
                print ("Leaves:", node.leaves())

            getNodes(node)
        else:
            list_node.append(node)
            
    return list_node
    
 # Lance le post tagging
def post_ta(text,show=1):  
    words=[]
    postag=[]
    for i in ne_chunk(pos_tag(word_tokenize(text))):
        if type(i) is nltk.Tree:
            lst_nde = getNodes(i)
            for n in lst_nde:
                words.append(n[0])
                postag.append(n[1])
        else:
            words.append(i[0])
            postag.append(i[1])
    if show >0:
        print(words,'\n',postag)
    return words,postag

w,p=post_ta(' '.join(sans_stop_words),show=0)
print(w,"\n",p)

"""============================================================================
    write json
============================================================================"""

for d in dict_filtering:
    idict = dict_filtering[d]
    ifile = d + '_filtering.json'
    with open(path_target + '/' + ifile, 'w', encoding = 'utf-8') as outfile:
        json.dump(idict, outfile)

print('End writing !')






