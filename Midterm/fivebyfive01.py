import sys
import random

d = {'one':[],'two':[],'three':[],'four':[],'five':[]}

words = []

for line in sys.stdin:
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

print d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+'.'
print d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+'.'
print d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+'.'
print d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+'.'
print d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+'.\n'

print d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+'.'
print d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+'.'
print d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+'.'
print d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+'.'
print d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+'.\n'

print d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+'.'
print d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+'.'
print d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+'.'
print d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+'.'
print d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+'.\n'

print d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+'.'
print d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+'.'
print d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+'.'
print d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+'.'
print d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+'.\n'

print d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+'.'
print d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+'.'
print d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+'.'
print d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+'.'
print d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+' '+d['five'][random.randint(0, len(d['five'])-1)]+'.\n'
