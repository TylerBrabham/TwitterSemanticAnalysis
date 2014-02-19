import urllib
import json

for i in range(11):
	if i==0:
		response = urllib.urlopen("http://search.twitter.com/search.json?q=microsoft")
	else:
		response = urllib.urlopen("http://search.twitter.com/search.json?q=microsoft&page="+str(i))

	tweets = json.load(response)
	results = tweets[u"results"]
	for tabs in results:
		print (tabs[u"text"]).encode('utf-8')+"\n"