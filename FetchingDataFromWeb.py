import requests

import os

#Movie, Currency Exchange Rate, and ZipCode API

#Movie API
#Referenced the class example
key = os.environ['omdb_key']

base_url = 'http://www.omdbapi.com/'

movie = input('What Movie Name?')

params = { 'apikey' : key, 't' : movie }
data = requests.get(base_url, params).json()

print(data['Ratings'][0]['Value']+'\n')


#Currency Exchange Rate Api
#Referenced Slack Channel software_dev_capstone, Scott Kim
base_url2 = 'https://api.fixer.io/latest?base=USD'

data2 = requests.get(base_url2).json()
date = data2["date"]
eur = str(data2["rates"]["EUR"])

print("Exchange Rate on " + date + ": 1 USD to " + eur + " EUR"+'\n')


#ZipCode API
key3 = os.environ['zipcode_key']

zipcode = input('Enter ZipCode: ')
distance = input('Return Zip Codes within a radius of how many miles: ')

base_url3 = 'https://www.zipcodeapi.com/rest/' + key3 + '/radius.json/' + zipcode +\
    '/' + distance + 'mile'

data3 = requests.get(base_url3).json()

zipcodes = data3['zip_codes']

for x in zipcodes:
    print('Zip Code ' + x['zip_code'] + ' is ' + str(x['distance']) + ' miles away')

