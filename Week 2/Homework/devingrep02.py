# our very first program!
import sys

for line in sys.stdin:
	line = line.strip()

	#if "' " in line:
	#	newline = line.replace("and","\n")
	#	print newline.replace("dreamin'","screamin'")
	
	#if "him" in line or "he" in line or "his":
	#	print line

	if "you" in line or "your" in line or "you're" in line:
		newline1 = line.replace("you're","")
		newline2 = newline1.replace("your","")
		newline3 = newline2.replace("you","")
		newline4 = newline3.replace("him","")
		newline5 = newline4.replace("his","")
		print newline5