import sys
import json

tweet_file = open(sys.argv[1])

total_word_count = 0
word_and_count = {}
for line in tweet_file:
	tweet_data = json.loads(line)
	if "text" in tweet_data:
		tweet = tweet_data["text"].encode("utf-8")
 		for word in tweet.split(' '):
 			total_word_count+=1
 			cleaned_word = word.replace('\n','')
 			if cleaned_word in word_and_count:
 				word_and_count[cleaned_word] += 1
 			else:
 				word_and_count[cleaned_word] = 1

for word in word_and_count:
	word_and_count[word] = float(word_and_count[word])/float(total_word_count)
 	print str(word)+' '+str(word_and_count[word])
