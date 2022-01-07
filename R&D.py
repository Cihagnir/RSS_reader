
from  bs4 import BeautifulSoup
import requests

url = 'https://feeds.simplecast.com/qm_9xx0g'

html_file = requests.get(url)

raw_html = BeautifulSoup(html_file.text,'html.parser')

news_title = raw_html.find_all("title")[1:5]
news_link = raw_html.find_all("link")[1:5]
raw_news_dscrp = raw_html.find_all("description")[1:]
news_dscrp = list()



for i in raw_news_dscrp:

    try:
        text = i.text.split("p>")[1]
        lenght = len(text)

        while True :
            try:
                start = text.index("<")
                end = text.index(">")
                text = text[0:start] + text[end+1:lenght]

            except ValueError:
                text = text[0:start]
                break
    except IndexError:
        text = i.text

    print(text)
