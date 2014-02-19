import sys
import json

tweet_file = open(sys.argv[1])

hash_and_count = {}
for line in tweet_file:
	tweet_data = json.loads(line)
	if "text" in tweet_data:
		hashtags = tweet_data["entities"]['hashtags']
		for tag in hashtags:
			clean_tag = tag[u'text'].encode("utf-8")
			if clean_tag in hash_and_count:
				hash_and_count[clean_tag]+=1
			else:
				hash_and_count[clean_tag] = 1

print_count = 0
while print_count<10:
	max_count = -float('inf')
	best_hash = None
	for hashes in hash_and_count:
		if hash_and_count[hashes]>max_count:
			max_count = hash_and_count[hashes]
			best_hash = hashes
	print best_hash+' '+str(float(hash_and_count[best_hash]))

	hash_and_count[best_hash] = -float('inf')
	print_count+=1