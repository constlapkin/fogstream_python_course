# task 5
# currency

import urllib

import urllib.request
from xml.etree import ElementTree

usd = "R01235"
eur = "R01239"

valute = ElementTree.parse(urllib.request.urlopen("http://www.cbr.ru/scripts/XML_daily.asp"))

valuteID = input("Task 5 | enter currency code: \n")
valuteID = valuteID.upper()

for i in valute.findall('Valute'):
    value = i.get('ID')
    if value == usd and valuteID == 'USD':
        rub = i.find('Value').text
        print("Dollar exchange rate: ", rub, " rubles")
    if value == eur and valuteID == 'EUR':
        rub = i.find('Value').text
        print("Euro exchange rate: ", rub, " rubles")
