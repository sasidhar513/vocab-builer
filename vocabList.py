import pickle;
import re;
import os;
from pathlib import Path;
import time

projectPath = str(Path().absolute())+'/'

engWords=[x.lower().strip() for x in open(projectPath+'src/words_final.txt','r').read().split()]

knownWords=pickle.load(open(projectPath+'out/PickleFiles/knownWords.pickle','rb'))
seenButForgotMeaning=pickle.load(open(projectPath+'out/PickleFiles/seenButForgotMeaning.pickle','rb'))
unKnownWords=pickle.load(open(projectPath+'out/PickleFiles/unKnownWords.pickle','rb'))
errorWords=pickle.load(open(projectPath+'out/PickleFiles/errorWords.pickle','rb'))


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
time.sleep(10)
	
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
	except:
		knownWords=list(sorted(set(knownWords)))
		seenButForgotMeaning=list(sorted(set(seenButForgotMeaning)))
		unKnownWords=list(sorted(set(unKnownWords)))
		errorWords=list(sorted(set(errorWords)))

		pickle.dump(knownWords,open(projectPath+'out/PickleFiles/knownWords.pickle','wb'))
		pickle.dump(seenButForgotMeaning,open(projectPath+'out/PickleFiles/seenButForgotMeaning.pickle','wb'))
		pickle.dump(unKnownWords,open(projectPath+'out/PickleFiles/unKnownWords.pickle','wb'))
		pickle.dump(errorWords,open(projectPath+'out/PickleFiles/errorWords.pickle','wb'))
		open(projectPath+'out/TextFiles/knownWords.txt','w').write('\n'.join(knownWords))
		open(projectPath+'out/TextFiles/seenButForgotMeaning.txt','w').write('\n'.join(seenButForgotMeaning))
		open(projectPath+'out/TextFiles/unKnownWords.txt','w').write('\n'.join(unKnownWords))
		open(projectPath+'out/TextFiles/errorWords.txt','w').write('\n'.join(errorWords))

knownWords=list(sorted(set(knownWords)))
seenButForgotMeaning=list(sorted(set(seenButForgotMeaning)))
unKnownWords=list(sorted(set(unKnownWords)))
errorWords=list(sorted(set(errorWords)))

pickle.dump(knownWords,open(projectPath+'out/PickleFiles/knownWords.pickle','wb'))
pickle.dump(seenButForgotMeaning,open(projectPath+'out/PickleFiles/seenButForgotMeaning.pickle','wb'))
pickle.dump(unKnownWords,open(projectPath+'out/PickleFiles/unKnownWords.pickle','wb'))
pickle.dump(errorWords,open(projectPath+'out/PickleFiles/errorWords.pickle','wb'))
open(projectPath+'out/TextFiles/knownWords.txt','w').write('\n'.join(knownWords))
open(projectPath+'out/TextFiles/seenButForgotMeaning.txt','w').write('\n'.join(seenButForgotMeaning))
open(projectPath+'out/TextFiles/unKnownWords.txt','w').write('\n'.join(unKnownWords))
open(projectPath+'out/TextFiles/errorWords.txt','w').write('\n'.join(errorWords))





