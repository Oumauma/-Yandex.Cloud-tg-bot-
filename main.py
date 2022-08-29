#  Copyright (c) Oumauma, 2022.

!pip install pygooglenews --upgrade
!pip install newspaper3k
!pip install pyTelegramBotAPI
!pip install GoogleNews 

from pygooglenews import GoogleNews
from newspaper import Article
import nltk
nltk.download('punkt')
import time

gn = GoogleNews()
crypto = gn.search('cryptocurrencies')
blockchain = gn.search('blockchain')

print(crypto['entries'][0]['title'])
article = Article(crypto['entries'][0]['link'])
article.download()
article.parse()
article.nlp()
print(article.summary)

channel = 'YourChannelName'

import telebot
token="YourToken"

bot = telebot.TeleBot(token)
aflink = 'YourLink'

first = True
while True:
  if first == True:
    crypto = gn.search('cryptocurrency')
    posted = crypto['entries'][0]['link']
    article = Article(crypto['entries'][0]['link'])
    article.download()
    article.parse()
    article.nlp()
    body = article.summary + '\n'
    head = '*'	+ crypto['entries'][0]['title'] + '*' + '\n\n'
    post = head + body + f'[Read more]({posted})\n\n' + f'[Support our channel]({aflink})'
    print(post)
    bot.send_message(channel, post, parse_mode='Markdown')
    first = False
    time.sleep(600)
  else:
    crypto = gn.search('cryptocurrency')	
    if posted != crypto['entries'][0]['link']:
      crypto = gn.search('cryptocurrency')
      posted = crypto['entries'][0]['link']
      article = Article(crypto['entries'][0]['link'])
      article.download()
      article.parse()
      article.nlp()
      body = article.summary + '\n\n'
      head = '*' + crypto['entries'][0]['title'] + '*' + '\n\n'
      post = head + body + f'[Read more]({posted})\n\n' + f'[Support our channel]({aflink})'
      print(post)
      bot.send_message(channel, post, parse_mode='Markdown')
      first = False
      time.sleep(600)
    else:
      time.sleep(600)
