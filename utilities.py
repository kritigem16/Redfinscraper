import sys
from bs4 import BeautifulSoup
from collections import OrderedDict


class Parser():

        def __init__(self):
                self.street_address='street_address'
                self.address_locality='address_locality'
                self.address_region='address_region'
                self.postal_code='postal_code'
                self.beds='beds'
                self.baths='baths'
                self.sold_on='sold date'
                self.price_per_sqF='price_per_sqFt'
                self.year_built='year_built'
                self.status='status'
                self.summary='summary'
                
        def parse_property_page(self, page_source, property_url):
       
                self.soup = BeautifulSoup(page_source, 'html.parser')
                property_data = OrderedDict()

                #  use try catch to handle when a data point is not available
                try:
                    property_data[self.street_address] = self.soup.find('span', attrs={'itemprop': 'streetAddress'}).get_text()
                except:
                    property_data[self.street_address] = 'N/A';print('street_address not found')
                try:
                    property_data[self.address_locality] = self.soup.find('span', attrs={'itemprop': 'addressLocality'}).get_text()
                except:
                    property_data[self.address_locality] = 'N/A';print('address_locality not found')
                try:
                    property_data[self.address_region] = self.soup.find('span', attrs={'itemprop': 'addressRegion'}).get_text()
                except:
                    property_data[self.address_region] = 'N/A';print('address_region not found')
                try:
                    property_data[self.postal_code] = self.soup.find('span', attrs={'itemprop': 'postalCode'}).get_text()
                except:
                    property_data[self.postal_code] = 'N/A';print('postal_code not found')
                try:
                    property_data[self.beds] = self.soup.find('div', attrs={'data-rf-test-id': 'abp-beds'}).find('div').get_text()
                except:
                    property_data[self.beds] = 'N/A';print('beds not found')
                try:
                    property_data[self.baths] = self.soup.find('div', attrs={'data-rf-test-id': 'abp-baths'}).find('div').get_text()
                except:
                    property_data[self.baths] = 'N/A';print('baths not found')
                try:
                    property_data[self.sold_on]=self.soup.find('div', attrs={'sash-text'}).get_text()
                except:
                    property_data[self.sold_on] = 'N/A';print('sold date not found') 
                try:
                    property_data[self.price_per_sqF] = self.soup.find('div', attrs={'data-rf-test-id': 'abp-sqFt'}).find('div',attrs={"data-rf-test-id": "abp-priceperft"}).get_text()
                except:
                    property_data[self.price_per_sqF] = 'N/A';print('price_per_sqFt not found')
                try:
                    property_data[self.year_built] = self.soup.find('span', attrs={"data-rf-test-id": "abp-yearBuilt"}).find('span', attrs={'class': 'value'}).get_text()
                except:
                    property_data[self.year_built] = 'N/A';print('year_built not found')
                try:
                    property_data[self.status] = self.soup.find('span', attrs={"data-rf-test-id": "abp-status"}).find('span',attrs={'class': 'value'}).get_text()
                except:
                    property_data[self.status] = 'N/A';print('status not found')

                property_data[self.summary] = self.soup.find('div', attrs={'class': 'remarks'}).get_text()
                
               
                return property_data

   
