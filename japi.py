#Cameron George and Chelsea Gomolka
import sys
import json
import urllib.request
import pandas as pd
from alpha_vantage.timeseries import TimeSeries

QUERY_URL = "https://www.alphavantage.co/query?function={REQUEST_TYPE}&apikey={KEY}&symbol={SYMBOL}"
API_KEY = 'O23LBUNG5OIVEI1Y'

def getStockData(symbol):
    try:
        print("Retrieving STONKS data...")
        timeSeries = TimeSeries(key=API_KEY, output_format='pandas')
        data, meta_data = timeSeries.get_intraday(symbol=symbol, interval='1min')
        return str(data.tail(1).iloc[0]['4. close'])
        
    except:
        return "not found"

def main():
    outFile = open('japi.out', 'w')
    while 1:
        userInput = input("Enter Stock Symbol or EXIT to Exit: ").upper()
        if userInput !="EXIT":
            serverData = 'The Current Price of {} is {}\n'.format(userInput, getStockData(userInput))
            print(serverData)
            outFile.write(serverData)
        else:
            sys.exit("\nComplete.\n")
main()

print("Stock Quotes Retrieved successfully!")
