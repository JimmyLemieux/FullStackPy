from bs4 import BeautifulSoup
import urllib as htttpParse
import requests
import re
from collections import defaultdict
import logging
import sys

class __Parse__:
    def __init__(self,PARSE_URL_BASE):
        try:
            self.resp = requests.get(PARSE_URL_BASE,stream=True)   #Should be surronded with try and catch
            self.SOUP = BeautifulSoup(self.resp.text,'html.parser') #encode to string
        except:
            print "Error in the URL/Connection port Failed"
            exit()

    def run_search(self):
		lawyer_name = [x.get_text() for x in self.SOUP.find_all('div', {'class':'lawyerName'})]
		lawyer_phone = [x.get_text() for x in self.SOUP.find_all('div', {'class' : 'lawyerPhone'})]
		lawyer_address = [x.get_text() for x in self.SOUP.find_all('div', {'class' : 'lawyerAddress'})]
		tup = zip(lawyer_name,lawyer_phone,lawyer_address)
		return tup


    def __out__(self,INFO):
			print INFO
            #####JUST TEST#####


class __Bulk__:
    def __init__(self):
        self.RESP_DICT = defaultdict(str)

    def record_info(self,INFO):
        for i in INFO:
            self.RESP_DICT[i[0]] = [i[1],i[2]]
        #self.RESP_DICT[INFO[0]] = zip(INFO[1],INFO[2])			#The info will be zipped into a tuple
        print '.',

    def __out__(self):
        return self.RESP_DICT

class fetch_data:

    def GET_PROGRESS(self,CURRENT_PAGE):
        sys.stdout.write(CURRENT_PAGE/75);
        sys.stdout.flush()

    def GET(self,CITY):
        print 'fetching in progress'
        bulk_recorder = __Bulk__()
        for PAGE in xrange(75):
            URL = "https://canadalawyerlist.com/city/{0}.html?page={1}".format(CITY,PAGE)
            p = __Parse__(URL) # Start to setup and gathering html information
            INFO = p.run_search()
            bulk_recorder.record_info(INFO)
        return bulk_recorder.__out__()
