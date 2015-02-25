import sys
import random

words = set()

for line in sys.stdin:
	line = line.strip()
	line = line.lower()
 	line_words = line.split()
 	for word in line_words:
		words.add(word)
	wordlist = list(words)

random.shuffle(wordlist)
output = " ".join(wordlist)
output = output.replace(", ","\n")
output = output.replace(". ","\n")
output = output.replace("! ","\n")
output = output.replace("? ","\n")
print output
