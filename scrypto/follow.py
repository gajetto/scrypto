# -*- coding: utf-8 -*-

from tweepy import OAuthHandler, API, Stream, TweepError
from tweepy.streaming import StreamListener
import os
import json
import telepot


consumer = os.environ.get("consumer_key")
secret = os.environ.get("consumer_secret")
access_key = os.environ.get("access_token_key")
access_secret = os.environ.get("access_token_secret")
bot_token = os.environ.get("telepot_token")



def hashtag (number):
    return '#'*number
def getTrack():
    file = "C:\\Users\\Ludovic\\Python\\scrypto\\scrypto\\spiders\\files\\track.txt"
    with open (file, 'r') as fichier:
        content = fichier.read()
        track= content.strip().split(',')
    return track





class FollowTwitterListener(StreamListener):
    def __init__(self, bot):
        self.bot = bot
        self.track = track

    def on_data(self, data):
        decoded = json.loads(data)
        try:
            num = decoded['user']['id_str']
            screen = decoded['in_reply_to_screen_name']
            text = decoded['text']
            time = decoded['created_at']
            name = decoded['user']['screen_name'].upper()
            if (num in users) and (screen == None) and ((' RT@' or ' RT @') not in text):
                text = text.replace(',','').replace(':','').replace('!','').replace('?','').replace('-','').replace('.','').replace('"','').strip()
                tweet = text.split(" ")
                for i in tweet:
                    if i in track:
                        message  = f'\n {name} \n Tweeted : {text} \n @{time} \n'
                        print(message)
                        self.bot.sendMessage(476895805, message)
                    break
        except KeyError as e:
            print("Error on retrieving coin user : %s" % str(e))
        return True

    def on_error(self, status_code):
        if status_code == 420:
            print('Got an error with status code: ' + str(status_code))
            return False
        return True  # To continue listening

    def on_timeout(self):
        print('Timeout...')
        return True  # To continue listening

    @classmethod
    def getCoinList(cls, api):
        users = list()
        filename = 'C:\\Users\\Ludovic\\Python\\scrypto\\scrypto\\spiders\\files\\links.txt'
        with open(filename, 'r', encoding='utf-8') as fichier:
            var = fichier.read()
            coins = var.strip().split('\n')
            for i, coin_name in enumerate(coins):
                try:
                    user = api.get_user(coin_name)
                    user = user.id_str
                    users.append(user)
                except TweepError as e:
                    print("Error on retrieving coin user : %s" % str(e))
                    print(coin_name)
        return users


if __name__ == '__main__':
    bot = telepot.Bot(bot_token)
    track = getTrack()
    follow_listener = FollowTwitterListener(bot, track)
    auth = OAuthHandler(consumer, secret)
    auth.set_access_token(access_key, access_secret)
    auth.secure = True
    api = API(auth)
    users = None
    try:
        users = FollowTwitterListener.getCoinList(api)
    except TweepError as e:
        print("Error on retrieving coin user : %s" % str(e))
    finally:
        stream = Stream(auth, follow_listener)
        stream.filter(follow=users)