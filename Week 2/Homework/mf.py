# our very first program!
import sys

# import random
# >>> words = ['fuck', 'shit', 'cock', 'piss']
# ['fuck', 'shit', 'cock', 'piss']
# >>> random.choice(words)

mf = "muthafuckin' "

for line in sys.stdin:
	line = line.strip()

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

	print line