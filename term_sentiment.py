import sys
import json

def hw(sent_file,tweet_file):
	sent_scores = {} # initialize an empty dictionary
	for line in sent_file:
 		term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
  		sent_scores[term] = int(score)  # Convert the score to an integer.

  	#print score of each tweet
  	tweet_score = 0
  	new_words = {}
  	unknwown_words = []
	for line in tweet_file:
		tweet_score = 0
	 	tweet_data = json.loads(line)
	 	unknown_words = []
	 	if "text" in tweet_data:
	 		tweet = tweet_data["text"].encode("utf-8")
	 		for word in tweet.split(" "):
	 			#lookup word in sent_file
	 			if word in sent_scores:
	 				tweet_score += sent_scores[word]
	 			else:
	 				unknown_words.append(word);
	 				
	 	for word in unknown_words:
	 		if word in new_words:
	 			new_words[word] += tweet_score
	 		else:
	 			new_words[word] = tweet_score
	for word in new_words:
	 	print word+' '+str(new_words[word])

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw(sent_file,tweet_file)

if __name__ == '__main__':
    main()
