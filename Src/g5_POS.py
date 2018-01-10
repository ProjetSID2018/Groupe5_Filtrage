import nltk
from nltk import ne_chunk, pos_tag
from nltk.tokenize import word_tokenize


#Goes through the POS-TAG tree if Tree not a tuple
def getNodes(parent):
    ROOT = 'ROOT'
    list_node = []
    for node in parent:
        if type(node) is nltk.Tree:
            getNodes(node)
        else:
            list_node.append(node)

    return list_node


#Adds POS-TAG in a parallel list
def pos_tagging(text, show=1):
    words = []
    postag = []
    for i in ne_chunk(pos_tag(word_tokenize(text))):
        if type(i) is nltk.Tree:
            lst_nde = getNodes(i)
            for n in lst_nde:
                words.append(n[0])
                if (n[0] in stop_words):
                    postag.append('STOPWORD')
                else:
                    postag.append(n[1])
        else:
            words.append(i[0])
            if (i[0] in stop_words):
                postag.append('STOPWORD')
            else:
                postag.append(i[1])
    if show > 0:
        print(words, '\n', postag)
    return words, postag