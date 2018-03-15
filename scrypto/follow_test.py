# -*- coding: utf-8 -*-

from tweepy import OAuthHandler, API, Stream, TweepError
from tweepy.streaming import StreamListener
import os
import json
import telepot


ids = ['4135644558', '2460502890', '1051053836', '2592325530', '862675563693125632', '3992601857', '2478439963', '2313671966', '1393174363', '2338506822', '2312333412', '759252279862104064', '894231710065446912',
 '4736263474', '908863693248593920', '908576143975919616', '773009781644677120', '889691121000996864', '831847934534746114', '711030662728437760', '704476690139885568', '4633094778',
 '4826209539', '2510084300', '2893133450', '808032684270354433', '877807935493033984', '3351041295', '811762043451801600', '734688391942524928', '707515829798182912', '774689518767181828', '3190865591',
  '503238457', '2925093697', '760049490187386880', '2349043879', '2235729541', '2571393578', '903434091650883586', '795669839369027584', '2895317462', '866969628534243332', '769457743807844352',
   '877078771366453248', '774791455680434176', '744075632997470208', '910110294625492992', '2266631022', '841424245938769920', '826699259441328128', '916215987199934464', '872984298973941764',
    '769430199985332228', '119060937', '9130922', '897349629385232388', '874348944570159106', '865963965649571840', '872093043305963521', '880423818594070528', '4020178512', '3023646139', 
    '890365489658122242', '4053977488', '869962138932002817', '773447880564731904', '2279318342', '862007728956485632', '946758251902881792', '767645185962455040', '2804855658', '857130360903274500', 
    '802952526542893061', '739770876808167424', '810263154458578944', '864152888720977921', '838079168537587712', '871853588540248064', '2904107388', '1322660676', '4871918301', '781574541164150785', 
    '2243862290', '835194759178244096', '902079725761376256', '2275810436', '878291606830542848', '3305325070', '2842476639', '902420345373765632', '839189962000039937', '888343534083944448', 
    '3094365867', '766155733234835456', '772745248363712512', '4585412124', '897652496461680640', '915590652167061504', '906057790707216384', '907209378331336705', '870261829037023234', '2806456582',
     '776078472477347840', '842473913997250566', '3448833448', '2611894398', '4711101020', '843014705618870273', '20356963', '725253338640617472', '908158324167675904', '345738416', '879923428794355714', 
     '884823833370390529', '873936272976474113', '4103294411', '2575764354', '867100084248469505', '950289002787057664', '888794609509433347', '3291830170', '2532881881', '869908314292924416', 
     '905044387347939328', '908617107218112512', '879705117641117697', '956053987324760066', '2917040642', '897349503816040448', '828668619986964480', '922416176340316161', '877706077873111040', '929649576151154689',
      '775658150179508224', '902422244764172288', '884529680757293056', '2893134987', '864347902029709314', '932489752044961792', '2386122979', '910589747491418112', '702852640816963584', '2167563187',
       '896999303708909568', '4792182482', '949198041872912384', '788621834392637441', '3318365565', '882330272280322050', '868837446938742786', '818371891937296384', '902050036384620545','892844938332966912', 
       '843372242381783044', '856193547976028161', '2366835468', '3031213163', '897547038233067521', '3111739836', '932870849128001536', '736586614797783040', '902262803557482496', '857795554767650816', 
       '875901175081644032', '2965296846', '900267964737478656', '918994376105197568', '915531221551255552', '763039521936203776', '2337791851', '926154221723975680', '879244998876708864',
 '900532456821932032', '885426541185818625', '895231138909659137', '2797935057', '2337136418', '2432540773', '3214742482', '805450407078203392', '912987663052836864', '1031080662', '2794894848', 
 '840228005372874753', '911172484254150657', '884936655437791232', '880470278408724481', '761588458095796224', '824914570070355968', '2937820937', '887696537400332289', '732169766450954240',
  '809512948788064257', '2550694741', '2289036295', '1201353103', '880558867968540672', '939038081964851201', '4693333172', '2412651932', '925725389938446337', '874806795293777920', '4263670287',
   '723270672986845184', '4884319753', '2863324024', '864653270836498432', '883448012059672577', '719994873491931136', '826744598273912832', '865213817466142724', '862662287202668546', '2425322684',
    '918011835554570240', '4252750574', '2739496430', '918637837733498881', '2946825834', '1457614386', '952494351346647045', '936495688434696192', '912636796504219648', '903617387643199488',
     '913324073823870977', '854624262782676992', '860231756867416066', '900723960547090432', '4847197905', '877250426575482880', '2321378298', '854054464717639681', '286728598', '894593514197196807',
      '2580216320', '3297860764', '2266309700', '2501522515', '888369106419953664', '776834983587643392', '431417121', '890022946848202753', '818911235286581248', '130876609', '806812777935437825',
       '3040234498', '2389017793', '3401609092', '882514901876457472', '858954415176396800', '718774766136532992', '803111252218155009', '749620531062800384', '2443058040', '812121371199164416', '4913720158',
        '915314841111420929', '787962463195193344', '876779976036540416', '916038000827449344', '899248007954264065', '912860011428057088', '917007096209723392', '946273319036137472', '2325992934',
         '2648931079', '4897921972', '880413992040222722', '711438260354953216', '780312880784764929', '944728504154943488', '874918556105940992', '896319102234443776', '4469439315', '2322494803'
, '753251908761055232', '2467468304', '907567124608102400', '895254960530636800', '906608437773074432', '862458216843628544', '922835747937357825', '2449701', '488068087', '885947368159498240',
'755918237867597824', '785214387007041536', '743468349649260545', '2159897706', '905462058107449345', '913182213994422272', '4794590665', '913471672090427393', '2741423690', '2361179618', '3323903998',
 '890522833381715968', '883335021943279618', '885770084295335936', '2444229696', '762578100563554304', '2485002769', '15632445', '1729661822', '856491395368013824', '844185333478637568',
'866740322994446337', '813969918760812544', '2347438777']



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
    def __init__(self, bot, track):
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

    stream = Stream(auth, follow_listener)
    stream.filter(follow=ids)