import sys
import random

def generate(filename):

	d = {'one':[],'two':[],'three':[],'four':[],'five':[]}

	words = []

	output = ""

	with open(filename, 'r') as f:
		lines = f.readlines()

	for line in lines:
		line = line.strip()
		line = line.lower()
	 	line_words = line.split()

	 	for word in line_words:
	 		if "'" in word:
				word = word.replace("'","")
			if "," in word:
				word = word.replace(",","")
			if "." in word:
	 			word = word.replace(".","")
			if "!" in word:
				word = word.replace("!","")
			if "?" in word:
				word = word.replace("?","")
			if "\"" in word:
				word = word.replace("\"","")
			if ";" in word:
				word = word.replace(";","")
			if ":" in word:
				word = word.replace(":","")
			if "(" in word:
				word = word.replace("(","")
			if ")" in word:
				word = word.replace(")","")
			if "-" in word:
				word = word.replace("-"," ")
			if "_" in word:
				word = word.replace("_","")
			if "/" in word:
				word = word.replace("/"," ")
			if '[' in word:
				word = word.replace("[","")
			if ']' in word:
				word = word.replace("]","")
			if '*' in word:
				word = word.replace("*","")
			if '@' in word:
				word = word.replace("@","")

			if len(word) == 1:
				d['one'].append(word)
			if len(word) == 2:
				d['two'].append(word)
			if len(word) == 3:
				d['three'].append(word)
			if len(word) == 4:
				d['four'].append(word)
			if len(word) == 5:
				d['five'].append(word)

	for i in range(0,5):
		for j in range(0,4):
			if j < 4:
				output = output + d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+'\n'
				j = j+1
			if j == 4:
				output = output + d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+'\n'+'\n'
		i = i+1

	return output