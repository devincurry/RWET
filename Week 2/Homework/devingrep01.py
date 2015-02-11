# our very first program!
import sys

for line in sys.stdin:
	line = line.strip()

	if "' " in line:
		newline = line.replace("and","\n")
		print newline.replace("dreamin'","screamin'")
	
	#if "will" in line or "won't" in line:
	#	print line

	#if "his" in line:
	#	print line.replace("his","her")
		#print line
		#print line.replace(" ","")