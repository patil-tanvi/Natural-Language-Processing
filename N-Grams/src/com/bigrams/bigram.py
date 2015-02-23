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
    n = 0
    for key in bigramFrequency.keys():
        freq = bigramFrequency.get(key)
        n += freq
        if freq in freqOfFreq:
            freqOfFreq[freq] += 1
        else:
            freqOfFreq[freq] = 1
    
    return freqOfFreq, n

def getBigramFreqTuring(bigramFrequency, freqOfFreq):
    
    bigramFreq = {}
    
    for key in bigramFrequency.keys():
        c = bigramFrequency.get(key)
        if(freqOfFreq.has_key(c + 1)):
            bigramFreq[key] = float( (c + 1) * (freqOfFreq.get(c + 1)) ) / float(freqOfFreq.get(c))
        
    return bigramFreq

def getBigramProbTuring(bigramFrequency, n):
    bigramFreqProb = {}
    for key1 in bigramFrequency.keys():
        count = bigramFrequency.get(key1)
        bigramFreqProb[key1] = float(count) / float(n)
        
    return bigramFreqProb

    