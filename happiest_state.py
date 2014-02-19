import sys
import json

def hw(sent_file,tweet_file):
	sent_scores = {} # initialize an empty dictionary
	for line in sent_file:
 		term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
  		sent_scores[term] = int(score)  # Convert the score to an integer.

  	#print score of each tweet
  	tweet_score = 0
  	states = {}
	for line in tweet_file:
		tweet_score = 0
	 	tweet_data = json.loads(line)
	 	if "text" in tweet_data and tweet_data['place']!=None:
	 		country = tweet_data['place']['country_code']
	 		if country=='US':
		 		tweet = tweet_data["text"].encode("utf-8")
		 		for word in tweet.split(" "):
		 			#lookup word in sent_file
		 			if word in sent_scores:
		 				tweet_score += sent_scores[word]

		 		full_name = (tweet_data['place']['full_name']).encode("utf-8")
		 		city, state =  full_name.split(', ')
		 		if state in states:
		 			states[state] += tweet_score
		 		else:
		 			states[state] = tweet_score

	#print the single happiest state
	max_happiness = -float('inf')
	happiest_place = None
	for state in states:
		if states[state]>max_happiness:
			max_happiness = states[state]
			happiest_place = state
	print happiest_place

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw(sent_file,tweet_file)

if __name__ == '__main__':
    main()
