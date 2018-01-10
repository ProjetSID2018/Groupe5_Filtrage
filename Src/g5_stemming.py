from nltk.stem.snowball import FrenchStemmer

def nltk_stemming(l_token):
    stemmer = FrenchStemmer()
    s = []
    for w in l_token:
        s.append(stemmer.stem(w))
    return s