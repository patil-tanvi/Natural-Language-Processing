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

matchObjRegEx1 = re.findall(r"([0-3]?[0-9][srnt]?[tdh]? (of)* ?(January|February|March|April|May|June|July|August|September|October|November|December)( ?,? '?[0-9][0-9]+)?)", fileText, flags=0)
#(January|February|March|April|May|June|July|August|September|October|November|December)
matchObjRegEx2 = re.findall(r"((January|February|March|April|May|June|July|August|September|October|November|December) [0-9][0-9]?[srnt]?[tdh]?( ?,? ((morning|afternoon|dawn|evening|dusk)* ?(of)? ?'?[0-9][0-9]+)?)?)", fileText, flags=0)
#(January|February|March|April|May|June|July|August|September|October|November|December) [0-9][0-9]?[a-z]?[a-z]?,? (morning|dawn|afternoon|evening)* ?(of)? ?'?([0-9][0-9])*

matchObjDays = re.findall(r"(Labor|Christmas Eve|Christmas|Memorial|Thanksgiving|New Year's|New Year|Martin Luther King,? Jr.) ?Day?", fileText, flags=0)

print(matchObjRegEx1)
print(matchObjRegEx2)
print(matchObjDays)
#Reg Ex1 : [0-3]?[0-9][a-z]?[a-z]? of? [A-Za-z]*,? [0-9]*
# Reg Ex 1 Modified : [0-3]?[0-9][a-z]?[a-z]? of? [A-Za-z]*,? ([0-9][0-9][0-9][0-9])?

#Reg Ex 2 : [A-Z][A-Za-z]* [0-9][0-9]?[a-z]*,? [0-9]*