from textblob import TextBlob
import sys
import random

filename1 = sys.argv[1]
filename2 = sys.argv[2]

output = ""

text1 = open(filename1).read().decode('ascii', errors='replace')
blob = TextBlob(text1)
np = blob.noun_phrases
verbs = []
nouns = []
adj = []
for word, pos in blob.tags:
	if pos == "VBP":
		if word != "are":
			verbs.append(word)
	if pos == "NNP":
		nouns.append(word)
	if pos == "JJ":
		adj.append(word)

text2 = open(filename2).read().decode('ascii', errors='replace')
blob = TextBlob(text2)
np.append(blob.noun_phrases)
# verbs2 = []
# nouns2 = []
for word, pos in blob.tags:
	if pos == "VBP":
		verbs.append(word)
	if pos == "NNP":
		nouns.append(word)
	if pos == "JJ":
		adj.append(word)

# for i in range(0,20):
#  	output = output + random.choice(nouns1) + " " + random.choice(nouns2) + " " + random.choice(verbs1) + " " + random.choice(nouns2) + ".\n"

output = output + "In " + random.choice(nouns) + " " + random.choice(verbs) + ", in " + random.choice(nouns) + " " + random.choice(verbs) + ", in " + random.choice(nouns) + " " + random.choice(verbs) + ".\n"
output = output + random.choice(verbs) + " " + random.choice(np) + " and " + random.choice(np) + " over the " + random.choice(nouns) + " of the " + random.choice(nouns) + ".\n"
output = output + "The " + random.choice(np) + " of " + random.choice(nouns) + " leads to the " + random.choice(np) + ".\n"
output = output + random.choice(nouns) + " is " + random.choice(np) + " courted by " + random.choice(nouns) + ".\n"
output = output + random.choice(nouns) + " that " + random.choice(verbs) + " but acts not, breeds " + random.choice(nouns) + ".\n"
output = output + "The " + random.choice(adj) + " " + random.choice(np) + " " + random.choice(verbs) + " the " + random.choice(nouns) + ".\n"
output = output + random.choice(verbs) + " " + random.choice(nouns) + " in the " + random.choice(nouns) + " that loves " + random.choice(nouns) + ".\n"
output = output + "A " + random.choice(nouns) + " sees not the same " + random.choice(nouns) + " that a " + random.choice(np) + " sees.\n"
output = output + random.choice(nouns) + " is in love with the " + random.choice(np) + " of " + random.choice(nouns) + ".\n"
output = output + "The " + random.choice(np) + " has no " + random.choice(nouns) + " for " + random.choice(nouns) + ".\n"
output = output + "The " + random.choice(nouns) + " of " + random.choice(nouns) + " are measured by the " + random.choice(nouns) + ", but of " + random.choice(nouns) + ": no " + random.choice(nouns) + " can measure.\n"
output = output + "All " + random.choice(np) + " is caught without a " + random.choice(nouns) + " or a " + random.choice(nouns) + ".\n"
output = output + "Bring out " + random.choice(np) + " in a " + random.choice(nouns) + " of " + random.choice(np) + ".\n"
output = output + "No " + random.choice(nouns) + " soars too " + random.choice(adj) + " if it soars with its own " + random.choice(nouns) + ".\n"
output = output + "A " + random.choice(adj) + " " + random.choice(np) + " " + random.choice(verbs) + ", not " + random.choice(verbs) + ".\n"
output = output + "The most " + random.choice(adj) + " act is to " + random.choice(verbs) + " another before you.\n"
output = output + "If the " + random.choice(nouns) + " would persist in " + random.choice(nouns) + ", it would become " + random.choice(adj) + ".\n"
output = output + random.choice(nouns) + " is the " + random.choice(nouns) + " of " + random.choice(np) + ".\n"
output = output + random.choice(nouns) + " is " + random.choice(nouns) + "'s " + random.choice(nouns) + ".\n"


for line in output:
	line = line.strip()
	for word in line:
		if "ai " in line:
			word = word.replace("ai ","ain't ")
print output