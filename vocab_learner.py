import pickle;
import re;
import os;
from pathlib import Path;
import time
from collections import defaultdict

projectPath = str(Path().absolute())+'/'
dictionary={}	
for i in 'abcdefghijklmnopqrstuvwxyz':
	temp=pickle.load(open(projectPath+'out/PickleFiles/dictionary/dictionary_'+i+'.pickle','rb'))
	dictionary = dict(dictionary, **temp)
	
def define(word):
	path=str(Path().absolute())+'/'
	if word not in dictionary.keys() or not dictionary[word]:
		output=''
		output+='\n----------------------------------------------------------\n'
		output+=word+'\n\tNo definition found for the the given word\n'
		output+='----------------------------------------------------------\n'
		return output
	else:
		output=''
		output+='\n\n----------------------------------------------------------\n'
		output+=word+'\n'
		for pos in dictionary[word].keys():
			output+='\t'+pos+'\n'			
			for meaning in dictionary[word][pos]:
				output+='\t\t'+meaning.capitalize()+'\n'				
		output+='----------------------------------------------------------'
		return output

knownWords=pickle.load(open(projectPath+'out/PickleFiles/learning/knownWords.pickle','rb'))
seenButForgotMeaning=pickle.load(open(projectPath+'out/PickleFiles/learning/seenButForgotMeaning.pickle','rb'))
unKnownWords=pickle.load(open(projectPath+'out/PickleFiles/learning/unKnownWords.pickle','rb'))
errorWords=pickle.load(open(projectPath+'out/PickleFiles/learning/errorWords.pickle','rb'))

allFiles=os.listdir(projectPath+'books')
allWords=[]
errors=[]
seen=[]
knows=[]
unknowns=[]
for eachFile in allFiles:
	words=[re.sub(r"[^a-zA-Z0-9'\-]",r'',word)  for word in [x.lower().strip() for x in open(projectPath+'books/'+eachFile,'r').read().split()]]
	words=[re.sub(r'^\W*|\W*$',r'',x) for x in words]
	for word in set(words):
		if word in errorWords:
			errors.append(word)
		elif word in knownWords:
			knows.append(word)
		elif word in seenButForgotMeaning:
			seen.append(word)
		elif word in unKnownWords:
			unknowns.append(word)


open(projectPath+'learn/knownWords.txt','w').write('\n'.join([define(x) for x in sorted(knows) if (x  in dictionary.keys() and dictionary[x])]))
open(projectPath+'learn/knownWords.txt','a').write('\n'.join([define(x) for x in sorted(knows) if (x not  in dictionary.keys()  or not dictionary[x])]))

open(projectPath+'learn/seenButForgotMeaning.txt','w').write('\n'.join([define(x) for x in sorted(seen) if (x  in dictionary.keys() and dictionary[x])]))


open(projectPath+'learn/seenButForgotMeaning.txt','a').write('\n'.join([define(x) for x in sorted(seen) if (x not  in dictionary.keys()  or not dictionary[x])]))
open(projectPath+'learn/unKnownWords.txt','w').write('\n'.join([define(x) for x in sorted(unknowns) if (x in dictionary.keys() and dictionary[x])]))
open(projectPath+'learn/unKnownWords.txt','a').write('\n'.join([define(x) for x in sorted(unknowns) if (x not  in dictionary.keys()  or not dictionary[x])]))

open(projectPath+'learn/errorWords.txt','w').write('\n'.join(sorted(errors)))




