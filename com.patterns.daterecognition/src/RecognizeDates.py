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

matchObjRegEx1 = re.findall(r"[0-3]?[0-9][a-z]?[a-z]? ?o?f? ?[A-Z][a-z]*,? '?[0-9]*", fileText, flags=0)
matchObjRegEx2 = re.findall(r"[A-Z][A-Za-z]* [0-9][0-9]?[a-z]?[a-z]?,? [a-z]* ?o?f? ?'?[0-9]*", fileText, flags=0)

print(matchObjRegEx1)
print(matchObjRegEx2)

#Reg Ex1 : [0-3]?[0-9][a-z]?[a-z]? of? [A-Za-z]*,? [0-9]*
# Reg Ex 1 Modified : [0-3]?[0-9][a-z]?[a-z]? of? [A-Za-z]*,? ([0-9][0-9][0-9][0-9])?

#Reg Ex 2 : [A-Z][A-Za-z]* [0-9][0-9]?[a-z]*,? [0-9]*