from playsound import playsound
import pandas as pd
import datetime as dt
import praw
import spacy
import csv
import os

clear = lambda: os.system('cls')
nlp = spacy.load('en_core_web_sm')

#setting up the reddit api
reddit = praw.Reddit(client_id = 'fzZIGmSl6rA3JQ', \
                     client_secret = 'Eck1_Gz1pC8tnNGIci4OIAfnIOXUEw', \
                     user_agent = 'meme', \
                     username = 'endpiN', \
                     password = 'maxrox2020')

subreddit = reddit.subreddit('wallstreetbets')

print("Loading stock tickers...")
with open('tickers.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)
clear()

print("Complete.")

run = True
mention_dict = {}
banned_words = ["a","open","for","one","it","now","two","all","am","or","out","he","big","are","on","can","see","has","next","beat","home","dd","rh"]
post_id_list = []

while run == True:

    for submission in subreddit.new(limit=1):
        try:
            title = submission.title
            post_id = submission.id
            title_doc = nlp(title)
            for word in title_doc:
                for ticker in data:
                    #print(word, ticker[0])
                    if (str(word) == str(ticker[0])) and not (str(word).lower() in banned_words) and not (post_id in post_id_list):
                        print(word)
                        post_id_list.append(post_id)
                        if str(word) not in mention_dict:
                            mention_dict[str(word)] = 1
                        else:
                            mention_dict.update({str(word): (mention_dict[str(word)] + 1)})
                            print(mention_dict)
        except Exception as e:
            raise e
