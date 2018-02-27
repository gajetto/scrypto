statuses = None
count = 0
isTweet, isFirst = False, True
try:
	statuses = api.user_timeline(id=user.id)
except TweepError as e:
	print(e.reason)
        for status in statuses:
            if isFirst:
                print('#'*25, status.user.screen_name , '#'*25 , '\n')
                print(f'followers count for {coin_name} is : ', user.followers_count)
                isFirst = False
            try:
                if status.created_at.date() == date.today():
                    print("created at : ", status.created_at , "\n")
                    print("@", status.text, '\n')
                    count+=1
                    isTweet = True
            except TweepError as e:
                print(e.reason)
                continue
            except StopIteration:
                break
            
        print(f'there are {count} tweets for {coin_name} today \n')
        print('#'*25 , i,"/",len(coins), '#'*25, '\n')       
                #print("Tweet id: " + status.id_str)
                #print(status.text)
                #print("Retweet count: " + str(status.retweet_count))
                #print("Favorite count: " + str(status.favorite_count))