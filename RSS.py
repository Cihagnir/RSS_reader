import sqlite3
from bs4 import BeautifulSoup
import requests

class class_RSS_reader(object):

    def __init__(self):
        db_conect = sqlite3.connect("RSS_link.db")
        db_cursor = db_conect.cursor()
        db_cursor.execute("Select * from RSS_LINK")
        self.list_RSS = db_cursor.fetchall()
        self.db_conect.commit()


    def get_scracth(self,web_link):
        list_return = list()

        html_file = requests.get(web_link)
        raw_html = BeautifulSoup(html_file.text,'html.parser')

        news_title = raw_html.find_all("title")[2:6]
        news_link = raw_html.find_all("link")[2:6]
        news_dscrp = raw_html.find_all("description")[1:5]

        for dscrp,link,title in zip(news_dscrp,news_link,news_title):
            # We get the news title and link
            R_title = title.text
            R_link = link.nextSibling

            try:
                # In here we clean the describtion text from html tags
                dscrp = dscrp.text.split("p>")[1]
                lenght = len(dscrp)

                while True:
                    try:
                        start = dscrp.index("<")
                        end = dscrp.index(">")
                        dscrp = dscrp[0:start] + dscrp[end+1:lenght]

                    except ValueError:
                        dscrp = dscrp[0:start]
                        break
            except IndexError:
                dscrp = dscrp.text

            splited_dscrp = dscrp.split(".")[0:-1]
            R_dscrp = ""
            try:
                for index in range(3):
                    R_dscrp += splited_dscrp[index]+".\n"

            except IndexError:
                pass

            list_return.append((R_title,R_dscrp,R_link))

        return list_return



    def add_RSS(self,website_name,website_link):
        db_conect = sqlite3.connect("RSS_link.db")
        db_cursor = db_conect.cursor()
        db_cursor.execute("Insert into RSS_LINK Values(?\ ?) ",(website_name,website_link))
        db_conect.commit()



RSS_reader = class_RSS_reader()






















