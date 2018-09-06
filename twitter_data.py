import tweepy

consumer_key = "5VK8LjqeedkkhUCktDu4XsSd3"
consumer_secret = "UylSTSKUEzmL9EyjdGPjwFai2LS0vD4y75smf24z7N5d8VeoIC"

access_token = "227449172-UDe4SMobVp3JBTUvqjiAgK8IjlvM8FqK7monS0bV"
access_token_secret = "1UVskkK5MQ5byfCDVYTUGgAbkqwoDrtvl2uUJKW2epIK7"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
public_tweets = api.home_timeline()

file = open('data.csv', 'w')
# print(public_tweets)
file.write('date,text,url_imagen,categoria\n')
"""
stuff = api.user_timeline(screen_name = 'luisevivanco', count = 5, include_rts = True)

for status in stuff:
    print(str(status._json).encode("utf-8"))


for tweet in public_tweets:
    print(str(tweet.keys()).encode("utf-8"))
    print(api.me)
"""

def get_data(hashtag, categoria):
    for tweet in tweepy.Cursor(api.search,q="#" + hashtag + " #guayaquil",count=200, since="2018-08-01").items():
        img_urls = ''
        if 'media' in tweet.entities:
            for image in  tweet.entities['media']:
                #print(str(image['media_url']), end='|')
                img_urls += str(image['media_url']) + '|'
            #print('\n')
        try:
            text = str(tweet.text).replace('\n',' ')
            linea = '' + ',"' + text + '",' + img_urls + ',' + categoria + '\n'
            print(linea)
            file.write(linea)
        except:
            pass


get_data('concierto', 'cultural')
get_data('teatro', 'cultural')
get_data('danza', 'cultural')
get_data('pintura', 'cultural')
get_data('futbol', 'deportivo')
get_data('baloncesto', 'deportivo')
get_data('baseball', 'deportivo')
get_data('deporte', 'deportivo')
get_data('cultura', 'cultural')
