import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')

def get_stopwords():
    return set(stopwords.words('french'))