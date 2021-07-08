import tweepy
import time

API_key = "your api key"
API_secret_key = "your api secret key"
access_token = "your access token"
Access_token_secret = "your secret access token"

# Authenticate to Twitter
auth = tweepy.OAuthHandler(API_key, API_secret_key)
auth.set_access_token(access_token, Access_token_secret)
api = tweepy.API(auth)

FILE_NAME = "last_seen.txt" #tweet id

def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id

def store_last_seen(FILE_NAME, last_seen_id):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return

def reply():
    last_seen_id = read_last_seen(FILE_NAME)
    mentions = api.mentions_timeline(last_seen_id, tweet_mode = 'extended')
    for mention in reversed(mentions):
        print(str(mention.id)+ '---' + mention.full_text)
        last_seen_id = mention.id
        store_last_seen(FILE_NAME, last_seen_id)
        #mention.
        if '@vampire_papi' in mention.full_text.lower():
            print("tagged master")
            api.update_status("@"+ mention.user.screen_name + " hello @"+ mention.user.screen_name + " you mentioned my master @vampire_papi, he will reply you soon. Have a good day :)", in_reply_to_status_id = last_seen_id)
        else:
            print("master not tagged")
            api.update_status("@"+ mention.user.screen_name + " @"+ mention.user.screen_name + "👍", in_reply_to_status_id = last_seen_id)
        #mention.id.favorites()

def searchbot(hashtag):
    for tweet in api.search(q=hashtag+'-filter:favorites', lang="en", rpp=1):
        try:
            #tweet.favorite()
            # if not tweet.favorited:
            #     tweet.favorite()
            if tweet.favorited is False:
                tweet.favorite()
            tweet.retweet()
            print(hashtag)
            #print(tweet.text)
            time.sleep(3)
            api.update_status(" Helpful...Take my upvote 👍", in_reply_to_status_id = tweet.id , auto_populate_reply_metadata=True)
            #api.update_status("@"+ tweet.user.screen_name + " Helpful...Take my upvote 👍", in_reply_to_status_id = tweet.id_str)
            time.sleep(600)
        except tweepy.TweepError as e:
            print(e)
            time.sleep(120)

hashtag = ['#python','#programming','#dsa','#100daysofcode','#PythonProgramming','#algorithms','#MachineLearning','#AI','#DataScience','#cpp','#c++','#codechef','#Flask','#django','#stackoverflow','#cybersecurity','#githubcopilot']
while True:
    reply()
    time.sleep(600)
    for hash_tag in hashtag:
        searchbot(hash_tag)
