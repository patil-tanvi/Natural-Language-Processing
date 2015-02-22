from FileFuncs import getTextFromFile
from com.unigram import getUnigram
from decimal import Decimal
from com.bigrams import getBigrams, getBigramProb, getBigramLaplaceProb
import math

unigramFrequency = dict()
bigramFrequency = dict()
bigramFrequencyProbability = dict()

def normalizeString(text):
    text = text.replace('\n',' ')
    text = text.lower()
    return text

def getSentenceProbability(testInput, withLaplace):
    global bigramFrequencyProbability
    
    prob = float(0)
    vocabulary = len(unigramFrequency)
    if withLaplace == False:
        bigramFrequencyProbability = getBigramProb(bigramFrequency, unigramFrequency)
    else:
        bigramFrequencyProbability = getBigramLaplaceProb(bigramFrequency, unigramFrequency)
    
    prev = ''
    
    newWordProb = float(1) / float(vocabulary)
    
    for word in testInput.split():
        if prev != '' :
            if withLaplace == False:
                if(bigramFrequency.has_key(prev + ' ' + word)):
                    prob = prob + math.log(bigramFrequency.get(prev + ' ' + word))
            else:
                if(bigramFrequency.has_key(prev + ' ' + word)):
                    prob = prob + math.log(bigramFrequency.get(prev + ' ' + word))
                else:
                    prob = prob + math.log(newWordProb)
        prev = word
    
    return prob

def trainBigram():
    global unigramFrequency
    global bigramFrequency 
   
    text = getTextFromFile()
    text = normalizeString(text)
    unigramFrequency = getUnigram(text)
    bigramFrequency = getBigrams(text)
    
    return
    
def testBigram(withLaplace):
    testInput1 ='The company chairman said he will increase the profit next year .'
    testInput2 = 'The president said he believes the last year profit were good .'
    testInput1 = normalizeString(testInput1)
    testInput2 = normalizeString(testInput2)
    
    prob1 = getSentenceProbability(testInput1, withLaplace);
    prob2 = getSentenceProbability(testInput2, withLaplace);

    if(prob1 > prob2):
        print('1')
    else:
        print('2')
    
    return

trainBigram()
testBigram(False)
testBigram(True)