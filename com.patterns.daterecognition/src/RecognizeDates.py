'''
Created on Feb 3, 2015

@author: tanvi
'''
import FileFuncs
from FileFuncs import getTextFromFile
import re

fileText = getTextFromFile()
fileText = fileText.replace('\n',' ')

matchObjRegEx1 = re.findall(r"([0-3]?[0-9][srnt]?[tdh]? ?(morning|afternoon|dawn|evening|dusk)* (of)* ?(January|February|March|April|May|June|July|August|September|October|November|December)( ?,? '?[0-9][0-9]+)?)", fileText, flags=0)
matchObjRegEx2 = re.findall(r"((January|February|March|April|May|June|July|August|September|October|November|December) [0-9][0-9]?[srnt]?[tdh]?( ?,? ((morning|afternoon|dawn|evening|dusk)* ?(of)? ?'?[0-9][0-9]+)?)?)", fileText, flags=0)
matchObjDays = re.findall(r"(Labor|Christmas Eve|Christmas|Memorial|Thanksgiving|New Year's|New Year|Martin Luther King,? Jr.) ?Day?", fileText, flags=0)

for date in matchObjRegEx1:
    print(date[0])
for date in matchObjRegEx2:
    print(date[0])
for date in matchObjDays:
    print(date[0])