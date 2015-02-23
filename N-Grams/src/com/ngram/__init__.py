from FileFuncs import getTextFromFile
from com.unigram import getUnigram
from decimal import Decimal
import math
from com.bigrams.bigram import getBigrams, getFreqOfFreq, getBigramFreqTuring,\
    getBigramProbTuring, getBigramProb, getBigramLaplaceProb

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
    global bigramFrequency
    global freqOfFreq
    
    probMatrix = dict()
    bigramCountMatrix = dict()
    
    prob = float(0)
    vocabulary = len(unigramFrequency)
    
    if withTuring == True:
        freqOfFreq, n = getFreqOfFreq(bigramFrequency)
        bigramFrequencyTemp = getBigramFreqTuring(bigramFrequency, freqOfFreq)
        bigramFrequencyProbability = getBigramProbTuring(bigramFrequencyTemp, n)
    elif withLaplace == False:
        bigramFrequencyProbability = getBigramProb(bigramFrequency, unigramFrequency)
    else:
        bigramFrequencyProbability = getBigramLaplaceProb(bigramFrequency, unigramFrequency)
        
    prev = ''


    totalProb = float(0)

    for word in testInput.split():
        prob = float(0)
        if prev != '' :
            if withTuring:  #Calculate probability with good turing
                if(bigramFrequencyProbability.has_key(prev + ' ' + word)):
                    prob = bigramFrequencyProbability.get(prev + ' ' + word)
                else:
                    prob = float(freqOfFreq.get(1))/float(n)
            else:
                if withLaplace == False:   #Calculate probability without laplace smoothing
                    if(bigramFrequencyProbability.has_key(prev + ' ' + word)):
                        prob = bigramFrequencyProbability.get(prev + ' ' + word)
                else:       #Calculate probability  laplace smoothing
                    if(bigramFrequencyProbability.has_key(prev + ' ' + word)):
                        prob = bigramFrequencyProbability.get(prev + ' ' + word)
                    else:
                        prob = float(1)/float(unigramFrequency.get(prev) + vocabulary)
            probMatrix[prev + ' ' + word] = prob
            if(prob != 0):
                totalProb += math.log(prob)
            if bigramCountMatrix.has_key(prev + ' ' + word):
                bigramCountMatrix[prev + ' ' + word] += 1
            else:
                bigramCountMatrix[prev + ' ' + word] = 1
        prev = word
    
    return totalProb, bigramCountMatrix, probMatrix

def trainBigram():
    global unigramFrequency
    global bigramFrequency 
   
    text = getTextFromFile()
    text = normalizeString(text)
    unigramFrequency = getUnigram(text)
    bigramFrequency = getBigrams(text)

    return
    
def testBigram(testInput1, testInput2, withLaplace, withTuring):
#     testInput1 ='The company chairman said he will increase the profit next year .'
#     testInput2 = 'The president said he believes the last year profit were good .'
#     testInput1 = raw_input('Enter sentence 1 : ')
#     testInput2 = raw_input('Enter sentence 2 : ')
    
    testInput1 = normalizeString(testInput1)
    testInput2 = normalizeString(testInput2)
    
    prob1 = 0
    prob2 = 0
    
    if(withTuring):
        prob1, bigramCountMatrix1, probMatrix1 = getSentenceProbability(testInput1, withLaplace, withTuring)
        prob2, bigramCountMatrix2, probMatrix2 = getSentenceProbability(testInput2, withLaplace, withTuring)
    else:
        prob1, bigramCountMatrix1, probMatrix1 = getSentenceProbability(testInput1, withLaplace, withTuring);
        prob2, bigramCountMatrix2, probMatrix2 = getSentenceProbability(testInput2, withLaplace, withTuring);
        
        
    print 'Bigram count matrix for sentence 1 : ', bigramCountMatrix1
    print 'Bigram count matrix for sentence 2 : ', bigramCountMatrix2
    print 'Probability Matrix for sentence 1 : ', probMatrix1
    print 'Probability Matrix for sentence 2 : ', probMatrix2
    print 'Probability of sentence 1 : ', prob1
    print 'Probability of sentence 2 : ', prob2
    
    if(prob1 > prob2):
        print 'Sentence 1 has more probability.'
    else:
        print 'Sentence 2 has more probability.'
    
    return

trainBigram()
testInput1 = raw_input('Enter sentence 1 : ')
testInput2 = raw_input('Enter sentence 2 : ')
testBigram(testInput1, testInput2, False, False) #Without Laplace Smoothing
print('\nWith Laplace Smoothing')
testBigram(testInput1, testInput2, True, False) #With Laplace Smoothing 
print('\nWith Good Turing')
testBigram(testInput1, testInput2, False, True)