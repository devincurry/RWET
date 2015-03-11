import urllib
import json
import sys
import random

nyturl = "http://api.nytimes.com/svc/search/v2/articlesearch.json?q=luxury&begin_date=20140101&end_date=20150101&fl=snippet&api-key="
apiKey = "your key goes here"
scrape = urllib.urlopen(nyturl + apiKey).read()

words = []

data = json.loads(scrape)

for item in data["response"]["docs"]:
	words.append(item["snippet"])

for line in words:
	line = line.strip()
	stuff = line.split(" ")
	random.shuffle(stuff)
	output = " ".join(stuff)
	print output