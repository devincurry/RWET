# our very first program!
import sys
for line in sys.stdin:
	line = line.strip()
	if "you" in line:
		print line
		#print line.replace("something","something")