import tweepy

consumer_key = "5VK8LjqeedkkhUCktDu4XsSd3"
consumer_secret = "UylSTSKUEzmL9EyjdGPjwFai2LS0vD4y75smf24z7N5d8VeoIC"

access_token = "227449172-UDe4SMobVp3JBTUvqjiAgK8IjlvM8FqK7monS0bV"
access_token_secret = "1UVskkK5MQ5byfCDVYTUGgAbkqwoDrtvl2uUJKW2epIK7"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
public_tweets = api.home_timeline()
# print(public_tweets)
"""
stuff = api.user_timeline(screen_name = 'luisevivanco', count = 5, include_rts = True)

for status in stuff:
    print(str(status._json).encode("utf-8"))


for tweet in public_tweets:
    print(str(tweet.keys()).encode("utf-8"))
    print(api.me)
"""
print("CONCIERTOS")
for tweet in tweepy.Cursor(api.search,q="#guayaquil #concierto",count=5, since="2018-08-01").items():
    #print (tweet.created_at, tweet.text)
    print(tweet.geo)

"""
print("\nTEATRO")
for tweet in tweepy.Cursor(api.search,q="#guayaquil #teatro",count=100, since="2018-08-01").items():
    #print (tweet.created_at, tweet.text)
"""
