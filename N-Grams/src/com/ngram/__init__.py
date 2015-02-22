from FileFuncs import getTextFromFile
from com.unigram import getUnigram
from decimal import Decimal
from com.bigrams import getBigrams, getBigramProb, getBigramLaplaceProb
import math

unigramFrequency = dict()
bigramFrequency = dict()
bigramFrequencyProbability = dict()
freqOfFreq = dict()

def normalizeString(text):
    text = text.replace('\n',' ')
    text = text.lower()
    return text

def getSentenceProbability(testInput, withLaplace, withTuring):
    global bigramFrequencyProbability
    global freqOfFreq
    
    prob = float(0)
    vocabulary = len(unigramFrequency)
    
    if withTuring == True:
#         freqOfFreq = getFreqOfFreq(bigramFrequency)
        print('srg')
    elif withLaplace == False:
        bigramFrequencyProbability = getBigramProb(bigramFrequency, unigramFrequency)
    else:
        bigramFrequencyProbability = getBigramLaplaceProb(bigramFrequency, unigramFrequency)
    
    prev = ''

    for word in testInput.split():
        if prev != '' :
            if withTuring:  #Calculate probability with good turing
                print("with turing")
            else:
                if withLaplace == False:   #Calculate probability without laplace smoothing
                    if(bigramFrequencyProbability.has_key(prev + ' ' + word)):
                        prob = prob + math.log(bigramFrequencyProbability.get(prev + ' ' + word))
                else:       #Calculate probability  laplace smoothing
                    if(bigramFrequencyProbability.has_key(prev + ' ' + word)):
                        prob = prob + math.log(bigramFrequencyProbability.get(prev + ' ' + word))
                    else:
                        prob = prob + math.log(float(1)/float(unigramFrequency.get(prev) + vocabulary))
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
    
def testBigram(withLaplace, withTuring):
    testInput1 ='The company chairman said he will increase the profit next year .'
    testInput2 = 'The president said he believes the last year profit were good .'
    testInput1 = normalizeString(testInput1)
    testInput2 = normalizeString(testInput2)
    
    if(withTuring):
        print('with turing')
    else:
        prob1 = getSentenceProbability(testInput1, withLaplace, withTuring);
        prob2 = getSentenceProbability(testInput2, withLaplace, withTuring);

    print(prob1)
    print(prob2)
    
    if(prob1 > prob2):
        print('1')
    else:
        print('2')
    
    return

trainBigram()
testBigram(False, False) #Without Laplace Smoothing
testBigram(True, False) #With Laplace Smoothing 
# testBigram(False, True)