from logging import BufferingFormatter
import re
from pathlib import Path

madLibsFile = open('madLibs.txt')#open the madlibs text file

madLibsContent = madLibsFile.read()#read the madlibs text file

madList = re.split(pattern= r"[\.\n ]", string = madLibsContent)#convert to a list based on regex of text file

madLibsFile.close()#close file


for i in range(len(madList)): #iterate through list replacing every instance with user input
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
    
    if madList[i] == '': #to fix the periods
        madList[i] = '.'


#print(madList)

madLib = ' '.join(madList) #making it into a string again

finalMadLib = madLib.replace(' .', '.') #fixing the periods

print(finalMadLib) #prints final mad lib

newMadLibsFile = open('newMadLibs.txt', 'w') #creating new file for new mad lib

newMadLibsFile.write(finalMadLib)

newMadLibsFile.close()
