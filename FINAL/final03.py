from textblob import TextBlob
import sys
import random

filename1 = sys.argv[1]
filename2 = sys.argv[2]

output = ""

text1 = open(filename1).read().decode('ascii', errors='replace')
blob = TextBlob(text1)
nouns1 = blob.noun_phrases
verbs1 = []
for word, pos in blob.tags:
	if pos == "VBP":
		verbs1.append(word)

text2 = open(filename2).read().decode('ascii', errors='replace')
blob = TextBlob(text2)
nouns2 = blob.noun_phrases
verbs2 = []
for word, pos in blob.tags:
	if pos == "VBP":
		verbs2.append(word)

for i in range(0,20):
 	output = output + random.choice(nouns1) + " " + random.choice(nouns2) + " " + random.choice(verbs1) + " " + random.choice(nouns2) + ".\n"

for line in output:
	line = line.strip()

print output