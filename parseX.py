from bs4 import BeautifulSoup
import urllib as htttpParse
import re
from collections import defaultdict
import logging

class __Parse__:
    def __init__(self,PARSE_URL_BASE):
        try:
             self.resp = htttpParse.urlopen(PARSE_URL_BASE)   #Should be surronded with try and catch
             self.SOUP = BeautifulSoup(self.resp,'html.parser') #encode to string
        except:
            print "Error in the URL/Connection port Failed"
            console.log("Exiting...")
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
    def GET(self,CITY,PAGE):
        print 'fetching in progress'
        bulk_recorder = __Bulk__()
        URL = "https://canadalawyerlist.com/city/{0}.html?page={1}".format(CITY,PAGE)
        p = __Parse__(URL) # Start to setup and gathering html information
        INFO = p.run_search()
        bulk_recorder.record_info(INFO)
        return bulk_recorder.__out__()
