from logging import BufferingFormatter
import re
from pathlib import Path

madLibsFile = open('madLibs.txt')

madLibsContent = madLibsFile.read()

madList = re.split(pattern= r"[\.\n ]", string = madLibsContent)

madLibsFile.close()

for i in range(len(madList)):
    if madList[i] == 'ADJECTIVE':
        print('Please enter an adjective:')
        newAdj = input()
        madList[i] = newAdj

    if madList[i] == 'NOUN':
        print('Please enter a noun:')
        newNoun = input()
        madList[i] = newNoun
    
    if madList[i] == 'VERB':
        print('Please enter a verb:')
        newVerb = input()
        madList[i] = newVerb
    
    if madList[i] == '':
        madList[i] = '.'


#print(madList)

madLib = ' '.join(madList)

finalMadLib = madLib.replace(' .', '.')

print(finalMadLib)

newMadLibsFile = open('newMadLibs.txt', 'w')

newMadLibsFile.write(finalMadLib)

newMadLibsFile.close()
