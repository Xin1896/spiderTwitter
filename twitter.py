import snscrape.modules.twitter as sntwitter
import pandas as pd

# query = "(from:elonmusk) until:2023-03-01 since:2023-03-17"
query="Quantitative Trading"
tweets = []
limit = 500


for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    
    # print(vars(tweet))
    # breakgit
    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.date, tweet.username, tweet.content,tweet.url])
        
df = pd.DataFrame(tweets, columns=['Date', 'User', 'Tweet','URL'])
print(df)

# to save to csv
df.to_csv(f'{query} tweets.csv')
