import sys 

import pickle;
import re;
import os;
from pathlib import Path;
import time
from collections import defaultdict
from PyDictionary import PyDictionary
dictionary1=PyDictionary()
argumentList = sys.argv 
alphabet=argumentList[1].lower()
dictionary={}
projectPath = str(Path().absolute())+'/'
for i in 'abcdefghijklmnopqrstuvwxyz':
	temp=pickle.load(open(projectPath+'out/PickleFiles/dictionary/dictionary_'+i+'.pickle','rb'))
	dictionary = dict(dictionary, **temp)
yesCount=0
noCount=0

for i in dictionary.keys():
    if not dictionary[i]:
            noCount+=1
    else:
            yesCount+=1
engWords=[y for y in [x.lower().strip() for x in open(projectPath+'src/words_final.txt','r').read().split()] if y.startswith(alphabet)]
print(len(engWords))
print(len(set(engWords)))
print("Total Defined words: "+str(yesCount))
print("Total Not Defined words: "+str(noCount))
time.sleep(5)


		

count=0
for word in engWords:
	print(str(count)+'. '+word)
	if word not in dictionary.keys():
		dictionary[word]=dictionary1.meaning(word)
		if count%10==0:
			pickle.dump(dictionary,open(projectPath+'out/PickleFiles/dictionary/dictionary_'+alphabet+'.pickle','wb'))
		if count%60==0:
			pickle.dump(dictionary,open(projectPath+'out/PickleFiles/dictionary/bkup/dictionary_'+alphabet+'_'+str(count)+'.pickle','wb'))
	count+=1
pickle.dump(dictionary,open(projectPath+'out/PickleFiles/dictionary/dictionary_'+alphabet+'.pickle','wb'))
pickle.dump(dictionary,open(projectPath+'out/PickleFiles/dictionary/bkup/dictionary_'+alphabet+'_'+str(count)+'_final.pickle','wb'))
