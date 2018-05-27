import re
from bs4 import BeautifulSoup
import requests #or you can use urlib httpParse
from collections import defaultdict

class CITY_PARSE:
    def __init__(self):
        PARSE_DICT = defaultdict(lambda x: "")
        URL = "https://canadalawyerlist.com/browse.php"
        req = requests.get(URL)
        soup = BeautifulSoup(req.text,'html.parser')
        prov = soup.find_all('h2')
        group = soup.find_all('div',{'class' : 'well well-sm clearfix cityList'})
        for key, value in enumerate(group):
            groupTXT = group[key].find_all('div',{'class' : 'cityEntry'})
            txt = [x.text for x in groupTXT]
            PARSE_DICT[prov[key].text] = txt
        print PARSE_DICT

while __name__ == '__main__':
    P = CITY_PARSE()
    break
