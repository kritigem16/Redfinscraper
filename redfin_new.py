import sys
from time import sleep
import requests
from bs4 import BeautifulSoup
from collections import OrderedDict
import re
import json
from random import choice, randint
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
reg_property_urls = re.compile('(/[A-Z][A-Z]/[A-Za-z\-/0-9]+/home/[0-9]+)')

user_agent_header = {'User-agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'}

class RedFin_soldhomes():
    def __init__(self):
        self.zipcode=input('Enter the zipcode:- ')
        self.url = 'https://www.redfin.com/zipcode/'+self.zipcode+'/recently-sold'
        self.session = requests.Session()
        self.use_selenium = False
        self.use_proxies = False
        self.output_data = []
        self.property_urls = []
        self.max_sleep=10
        self.min_sleep=5

    def rand_sleep(self,min_sleep,max_sleep):
        sleep(randint(min_sleep,max_sleep)) 

    def request_search_page(self, property_url):
        self.rand_sleep(self.min_sleep, self.max_sleep)
        return self.make_page_request(property_url)  

    def make_page_request(self, property_url):
        for i in range(10):
            http_response = self.session.get(property_url, headers=user_agent_header, verify=True)
            if http_response.status_code == 200: return http_response.text
            else: print('Request Error')

    def get_search_results(self):
        page_source = self.request_search_page(self.url)
        self.property_urls = reg_property_urls.findall(page_source.replace('\\u002F', '/'))
        self.property_urls = list(set(self.property_urls))
        print(str(len(self.property_urls)) + ' properties recently sold')

    def get_property_page(self, property_url,parser):
        page_source = self.make_page_request(property_url)
        return parser.parse_property_page(page_source, property_url)

    def get_property_data(self,parser):
        count = 0
        for property_url in self.property_urls:
            self.output_data.append(self.get_property_page('https://www.redfin.com' + property_url,parser))
            count += 1
            print('finished property ' + str(count))
            open('redfin_output.json', 'w').write(json.dumps(self.output_data, indent=4))

   
