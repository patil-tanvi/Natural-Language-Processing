'''
Created on Feb 3, 2015

@author: tanvi
'''

def getTextFromFile():
    fileName = raw_input('Enter file name : ')
    file = open(fileName, 'r')
    fileText = file.read()
    return fileText