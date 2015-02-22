
from collections import Counter

def getUnigram(words):
    word_dict = Counter(words.split())
    return word_dict