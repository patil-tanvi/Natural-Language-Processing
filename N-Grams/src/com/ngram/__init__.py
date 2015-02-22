from FileFuncs import getTextFromFile
from com.unigram import getUnigram
from decimal import Decimal
from com.bigrams import getBigrams, getBigramProb
import math

unigramFrequency = dict()
bigramFrequency = dict()
bigramFrequencyProbability = dict()

def normalizeString(text):
    text = text.replace('\n',' ')
    text = text.lower()
    return text

def getSentenceProbability(testInput):
    prob = float(0)
    
    prev = ''
    for word in testInput.split():
        if prev != '' :
            if(bigramFrequency.has_key(prev + ' ' + word)):
                prob = prob + math.log(bigramFrequency.get(prev + ' ' + word))
        prev = word
    
    return prob

def trainBigram():
    global unigramFrequency
    global bigramFrequency 
    global bigramFrequencyProbability
    text = getTextFromFile()
    text = normalizeString(text)
    unigramFrequency = getUnigram(text)
    bigramFrequency = getBigrams(text)
    bigramFrequencyProbability = getBigramProb(bigramFrequency, unigramFrequency)
    return
    
def testBigram():
    testInput1 ='The company chairman said he will increase the profit next year .'
    testInput2 = 'The president said he believes the last year profit were good .'
    testInput1 = normalizeString(testInput1)
    testInput2 = normalizeString(testInput2)
    
    prob1 = getSentenceProbability(testInput1);
    prob2 = getSentenceProbability(testInput2);
    
    if(prob1 > prob2):
        print('1')
    else:
        print('2')
    
    return

trainBigram()
testBigram()