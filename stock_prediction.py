import pandas as pd
import yfinance as yf
import numpy as np

def get_stock_data(ticker,start_date,end_date):
    stock_data = yf.Ticker(ticker).history(start=start_date,end=end_date).reset_index()
    return stock_data

def get_sp500(start_date,end_date):
    sp500_data = yf.Ticker("^GSPC").history(start=start_date, end=end_date).reset_index()
    return sp500_data

class DataProcessing:
    def __init__(self, data):
        for column in data.columns:
            setattr(self,column.lower(),np.array(data[column]))

    def gen_train_test(self,train_percent_len):
        self.Y_train = self.close[0:round(train_percent_len*(len(self.close)))]
        self.X_train = self.date[0:round(train_percent_len*(len(self.date)))]
        self.Y_test = self.close[round(train_percent_len*(len(self.close))):len(self.close)]
        self.X_test = self.date[round(train_percent_len*(len(self.date))):len(self.date)]

        return self.X_train, self.Y_train, self.X_test, self.Y_test