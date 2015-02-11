# our very first program!
import sys

import random

mf = ["muthafuckin' ","muthafuckin' ","fuckin' ","fuckin' ","bullshit ass ","straight up ","dirty ass ","wack ass ","weak ass "]

for line in sys.stdin:
	line = line.strip()


	line = line.replace(" a "," a " + random.choice(mf))
	line = line.replace("A ","A " + random.choice(mf))
	line = line.replace(" the "," the " + random.choice(mf))
	line = line.replace("The ","The " + random.choice(mf))
	line = line.replace(" an "," a " + random.choice(mf))
	line = line.replace("An ","A " + random.choice(mf))
	line = line.replace(" his "," his " + random.choice(mf))
	line = line.replace("His ","His " + random.choice(mf))
	line = line.replace(" her "," her " + random.choice(mf))
	line = line.replace("Her ","Her " + random.choice(mf))
	line = line.replace(" my "," my " + random.choice(mf))
	line = line.replace("My ","My " + random.choice(mf))
	line = line.replace(" your "," your " + random.choice(mf))
	line = line.replace("Your ","Your " + random.choice(mf))
	line = line.replace(" this "," this " + random.choice(mf))
	line = line.replace("This ","This " + random.choice(mf))
	line = line.replace("That ","That " + random.choice(mf))
	if " that you " in line:
		line = line.replace(" that you "," that you " + random.choice(mf))

	print line