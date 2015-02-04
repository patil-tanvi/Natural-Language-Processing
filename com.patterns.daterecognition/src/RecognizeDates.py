'''
Created on Feb 3, 2015

@author: tanvi
'''
import FileFuncs
from FileFuncs import getTextFromFile
import re

fileText = getTextFromFile()
fileText = fileText.replace('\n',' ')
print(fileText)

#matchObj = re.findall(r'[0-3]?[0-9][t][h] [o][f] [January|September]', fileText, flags=0)

#print(matchObj)

#[0-3]?[0-9][a-z]?[a-z]? of? [A-Za-z]*,? [0-9]*