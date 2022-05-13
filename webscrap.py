import requests
from bs4 import BeautifulSoup
import pandas as pd
import lxml

url="https://www.frameip.com"

#import le code l'url
reponse=requests.get(url)
soup=BeautifulSoup(reponse.text,"html.parser")
# items=soup.findAll('item')
# item=items[0]
# item.description.text
# news_items=[]A
# for i in items:
#     news_i={}
#     news_i['title']=i.title.text
#     news_i['description'] = i.title.text
#     news_i['pubdate'] = i.title.text
#     news_items.append(news_i)
