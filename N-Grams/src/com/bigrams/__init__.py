# import re
# from itertools import islice, izip
# from collections import Counter
import math

def getBigrams(text):
    words = text.split()
    prevWord = ''
    bigramFreq ={}
    
    for word in words:
        if prevWord != '':
            bigram = prevWord + ' ' + word
            if bigram in bigramFreq:
                bigramFreq[bigram] += 1
            else:
                bigramFreq[bigram] = 1
        
        prevWord = word    
     
    return bigramFreq

def getBigramProb(bigramFreq, unigramFrequency):
    
    bigramFreqProb = {}
    for key1 in bigramFreq.keys():
        word1 = key1.split()[0]
        count = bigramFreq.get(key1)
        bigramFreqProb[key1] = float(count) / float(unigramFrequency.get(word1))
#         bigramFreqProb[key1] = math.log(float(count)) - math.log(float(unigramFrequency.get(word1)))
    return bigramFreqProb

def getBigramLaplaceProb(bigramFreq, unigramFrequency):
    smoothingCount = 1
    vocabulary = len(unigramFrequency)
    
    bigramFreqProb = {}
    for key1 in bigramFreq.keys():
        word1 = key1.split()[0]
        count = bigramFreq.get(key1) + smoothingCount
        bigramFreqProb[key1] = float(count) / float(unigramFrequency.get(word1) + vocabulary)
#         bigramFreqProb[key1] = math.log(float(count)) - math.log(float(unigramFrequency.get(word1) + vocabulary))
    return bigramFreqProb

def getFreqOfFreq(bigramFrequency):
    
    freqOfFreq = dict()
    return freqOfFreq