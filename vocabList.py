import pickle
import re
import os
from pathlib import Path

'''
dictionary= open('dictionary.csv','r').read().split('\n')
(word,meaning)=[(x[0].lower(),x[1]) for x in [y.split('^^^') for y in words]]
dictionary=[(x[0].lower(),[x[1]+'^^^'+x[2]]) for x in [y.split('^^^') for y in words] if len(x)>2]
dictionaryMap={}
for k,v in dictionary:
	dictionaryMap.setdefault(k,[]).append(v)'''

projectPath = str(Path().absolute())+'/'

engWords=[x.lower().strip() for x in open(projectPath+'src/words_final.txt','r').read().split()]

knownWords=pickle.load(open(projectPath+'out/knownWords.txt','rb'))
seenButForgotMeaning=pickle.load(open(projectPath+'out/seenButForgotMeaning.txt','rb'))
unKnownWords=pickle.load(open(projectPath+'out/unKnownWords.txt','rb'))
errorWords=pickle.load(open(projectPath+'out/errorWords.txt','rb'))

allFiles=os.listdir(projectPath+'books')
for eachFile in allFiles:
	allWords=[x.lower().strip() for x in open(projectPath+'books/'+eachFile,'r').read().split()]
	for word in allWords:
		word=word.strip().lower()
		word=re.sub(r"[^a-zA-Z0-9'\-]",r'',word)
		try:
			if word not in engWords and word not in knownWords:
				print(word+' came in first if')
				errorWords.append(word)
			elif word in knownWords:
				knownWords.append(word)
			elif word in seenButForgotMeaning:
				seenButForgotMeaning.append(word)
				'''out=int(input('Are you sure you know the meaning for   '+   word +'   ??? \npress \n1 for I finally by hearted the meaning\n2 for No.'))
				if out == 1:
					[knownWords.append(x) for x in seenButForgotMeaning if x == word]
					seenButForgotMeaning.removeall('word')
				else:
					seenButForgotMeaning.append(word)'''
			elif word in unKnownWords:
				unKnownWords.append(word)
				'''
				out=int(input('Are you sure you got the idea of   '+   word +'   ??? \npress \n1 for I finally got the idea\n2 for No.'))
				if out == 1:
					[seenButForgotMeaning.append(x) for x in unKnownWords if x == word]
					unKnownWords.removeall('word')
				else:
					unKnownWords.append(word)'''
			else:
				out=int(input('This word is new to you::::   '+   word +'   ??? \npress \n1 if you know the word\n2 if you have an idea of the word but dont know the meaning\n3 if you didnt know the meaning of the word.\n'))
				if out == 1:
					knownWords.append(word)
				if out == 2:
					seenButForgotMeaning.append(word)
				if out == 3:
					unKnownWords.append(word)
		except:
			pickle.dump(knownWords,open(projectPath+'out/knownWords.txt','wb'))
			pickle.dump(seenButForgotMeaning,open(projectPath+'out/seenButForgotMeaning.txt','wb'))
			pickle.dump(unKnownWords,open(projectPath+'out/unKnownWords.txt','wb'))
			pickle.dump(errorWords,open(projectPath+'out/errorWords.txt','wb'))

	
		
				
	



