# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 11:29:34 2013

@author: skunath
"""

"""
A Stock class
    (should require minimal input)
    what stock is it?  (no input required)
    What price was it at at a certain point? (input of date/time)
    What was the trading volume on a particular day? (input of date/time)
    What are the total amount of stock outstanding
    
    other methods:
        calculate sharpe ratio (input of start and stop date)
        drawdown list (no input or single day as last point)
        max drawdown (start and stop range)

"""

class Stock:
    actual_stock_symbol = ""
    def __init__(self):
        pass
    
    def stock_symbol(self):
        print self.actual_stock_symbol
              
        #insert code chere
    def set_stock_symbol(self, new_symbol):
        self.actual_stock_symbol = new_symbol
        # code to set the stock symbol
        
    def validate_stock_symbol(self):
        pass
        #pull code form other place
        
    def get_price_at_date(self, date):
        pass
        # integrate from markitondemand
        
test =  Stock()