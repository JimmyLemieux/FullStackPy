import re
from bs4 import BeautifulSoup
import requests #or you can use urlib httpParse
import urllib as httpParse
from collections import defaultdict

class CITY_PARSE:
    def __init__(self):
        self.PARSE_DICT = defaultdict(lambda x: "")
        self.URL = "https://canadalawyerlist.com/browse.php"
        self.REQ = httpParse.urlopen(self.URL)
        self.SOUP = BeautifulSoup(self.REQ,'html.parser')

    def PARSE(self):
        prov = self.SOUP.find_all('h2')
        group = group = self.SOUP.find_all('div',{'class' : 'well well-sm clearfix cityList'})
        for key, value in enumerate(group):
            groupTXT = group[key].find_all('div',{'class' : 'cityEntry'})
            txt = [x.text for x in groupTXT]
            self.PARSE_DICT[prov[key].text] = txt
        return self.PARSE_DICT

while __name__ == '__main__':
    P = CITY_PARSE()
    CITY = P.PARSE()
    for i in CITY:
        print CITY[i]
    break
