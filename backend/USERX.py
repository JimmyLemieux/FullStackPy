import re
import logging
from parseX import fetch_data
import requests
import json
#TODO: Print out logo
#Enter province in Ontario
#Then city
#Run parse code

class USER_PROMPT:
    def __init__(self):
        with open('art','r') as f:
            print f.read()

    def USER_READ(self,p,CITY,PROV):
        #We will just read in the city for now
        if p.lower() == 'n':
            CITY = raw_input("Which city are you currently in..")
            print "Ok we will get on that...."
            INFO = fetch_data()
            GET = INFO.GET(CITY,1) #Going to take the number out
            print GET
        elif p.lower() == 'y':
            print "Ok we will get on that...."
            INFO = fetch_data()
            GET = INFO.GET(CITY,1) #Going to take the number out
            print GET

    def USER_LOCATION(self):
        send_url = "http://freegeoip.net/json"
        r = requests.get(send_url)
        j = json.loads(r.text)
        return j['city'],j['region_name']

while __name__ == '__main__':
    USER = USER_PROMPT()
    CITY,PROV = USER.USER_LOCATION()
    print "By our records, we can see that you are currently located in {0} : {1}".format(CITY,PROV)
    cur_search = raw_input("Would you like to search in this location? (y/n)")
    if(cur_search == 'y' or cur_search == 'n'):
        USER.USER_READ(cur_search,CITY,PROV)
    break
