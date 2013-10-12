# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 11:37:16 2013

@author: skunath
"""

import json
import requests


def validate_symbol(stock_symbol):
    payload = {'input': stock_symbol}
    headers = {'content-type': 'application/json'}
    response = requests.get('http://dev.markitondemand.com/Api/Lookup/json', params=payload, headers=headers)
    return_data = response.json()
    if len(return_data) == 0:
        print "No stock with symbol... try again."
    else:
        symbol_match = [1 for symbol in return_data if symbol["Symbol"].lower() == stock_symbol]
        if len(symbol_match) == 1:
            print  "exact match found"
        else:
            name_match = [1 for symbol in return_data if stock_symbol.lower() in symbol["Name"].lower()]
            if len(name_match) >= 1:
                print name_match
        
        print symbol_match

stock_symbol = raw_input("What stock do you wish to look at? --> ").lower()
while stock_symbol != "quit":
    validate_symbol(stock_symbol)
    stock_symbol = raw_input("What stock do you wish to look at? --> ").lower()



#send_data = {}
#send_data["symbol"]


