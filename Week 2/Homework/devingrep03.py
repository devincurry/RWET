# our very first program!
import sys

mf = "muthafuckin' "

for line in sys.stdin:
	line = line.strip()

	#if "' " in line:
	#	newline = line.replace("and","\n")
	#	print newline.replace("dreamin'","screamin'")
	
	#if "him" in line or "he" in line or "his":
	#	print line

	#if "a " in line or "the " in line or "an " in line or "this " in line or "that " in line:
	line = line.replace(" a "," a " + mf)
	line = line.replace("A ","A " + mf)
	line = line.replace(" the "," the " + mf)
	line = line.replace("The ","The " + mf)
	line = line.replace(" an "," a " + mf)
	line = line.replace("An ","A " + mf)
	line = line.replace(" this "," this " + mf)
	line = line.replace("This ","This " + mf)
	line = line.replace(" that "," that " + mf)
	line = line.replace("That ","That " + mf)




		#newline2 = newline1.replace("your","")
		#newline3 = newline2.replace("you're","")
		#newline4 = newline3.replace("him","")
		#newline5 = newline4.replace("his","")
	print line