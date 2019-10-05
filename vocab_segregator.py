import pickle;
import re;
import os;
from pathlib import Path;
import time
from collections import defaultdict
def save(knownWords,seenButForgotMeaning,unKnownWords,errorWords,projectPath):
	knownWords=list(sorted(set(knownWords)))
	seenButForgotMeaning=list(sorted(set(seenButForgotMeaning)))
	unKnownWords=list(sorted(set(unKnownWords)))
	errorWords=list(sorted(set(errorWords)))
	pickle.dump(knownWords,open(projectPath+'out/PickleFiles/learning/knownWords.pickle','wb'))
	pickle.dump(seenButForgotMeaning,open(projectPath+'out/PickleFiles/learning/seenButForgotMeaning.pickle','wb'))
	pickle.dump(unKnownWords,open(projectPath+'out/PickleFiles/learning/unKnownWords.pickle','wb'))
	pickle.dump(errorWords,open(projectPath+'out/PickleFiles/learning/errorWords.pickle','wb'))
	open(projectPath+'out/TextFiles/learning/knownWords.txt','w').write('\n'.join(knownWords))
	open(projectPath+'out/TextFiles/learning/seenButForgotMeaning.txt','w').write('\n'.join(seenButForgotMeaning))
	open(projectPath+'out/TextFiles/learning/unKnownWords.txt','w').write('\n'.join(unKnownWords))
	open(projectPath+'out/TextFiles/learning/errorWords.txt','w').write('\n'.join(errorWords))

projectPath=str(Path().absolute())+'/'
dictionary={}	
for i in 'abcdefghijklmnopqrstuvwxyz':
	temp=pickle.load(open(projectPath+'out/PickleFiles/dictionary/dictionary_'+i+'.pickle','rb'))
	dictionary = dict(dictionary, **temp)
	
def define(word):
	path=str(Path().absolute())+'/'
	if word not in dictionary.keys() or len(dictionary[word])==0:
		print('No definition found for the the given word')
		return;
	else:
		print ('----------------------------------------------------------')
		print(word)
		for pos in dictionary[word].keys():
			print('\t'+pos)					
			for meaning in dictionary[word][pos]:
				print('\t\t'+meaning)				
		print ('----------------------------------------------------------')
		



engWords=[x.lower().strip() for x in open(projectPath+'src/words_final.txt','r').read().split()]

knownWords=pickle.load(open(projectPath+'out/PickleFiles/learning/knownWords.pickle','rb'))
seenButForgotMeaning=pickle.load(open(projectPath+'out/PickleFiles/learning/seenButForgotMeaning.pickle','rb'))
unKnownWords=pickle.load(open(projectPath+'out/PickleFiles/learning/unKnownWords.pickle','rb'))
errorWords=pickle.load(open(projectPath+'out/PickleFiles/learning/errorWords.pickle','rb'))

allFiles=os.listdir(projectPath+'books')
allWords=[]
for eachFile in allFiles:
	words=[re.sub(r"[^a-zA-Z0-9'\-]",r'',word)  for word in [x.lower().strip() for x in open(projectPath+'books/'+eachFile,'r').read().split()]]
	words=[re.sub(r'^\W*|\W*$',r'',x) for x in words]
	for word in set(words):
		if word not in engWords:
			words.remove(word)
			errorWords.append(word)
	words=sorted(set([x for x in words if x not in knownWords and x not in seenButForgotMeaning  and x not in unKnownWords and x not in errorWords ]))
	allWords+=words

print ("Total count of unseen words in all Files:" + str(len(allWords)))
	
count=0
for word in allWords:
	count+=1
	print('Total words count is '+str(len(allWords))+'. Distinct words count is '+str(len(set(allWords)))+'. Completed word Count is '+str(len(knownWords)+len(errorWords)+len(seenButForgotMeaning)+len(unKnownWords))+'. Current word----->'+str(count)+': '+word)  
	try:
		if word not in engWords and word not in knownWords and word not in errorWords:
			pass
			
		elif word in errorWords:
			pass

		elif word in knownWords:
			pass

		elif word in seenButForgotMeaning:
			pass

		elif word in unKnownWords:
			pass
			
		else:
			out=int(input('This word is new to you::::   '+   word +'   ??? \npress \n1 if you know the word\n2 if you have an idea of the word but dont know the meaning\n3 if you didnt know the meaning of the word.\n'))
			if out == 1:
				knownWords.append(word)
			if out == 2:
				seenButForgotMeaning.append(word)
			if out == 3:
				unKnownWords.append(word)
		if count%10==0:
			save(knownWords,seenButForgotMeaning,unKnownWords,errorWords,projectPath)
	except:
		save(knownWords,seenButForgotMeaning,unKnownWords,errorWords,projectPath)
save(knownWords,seenButForgotMeaning,unKnownWords,errorWords,projectPath)






