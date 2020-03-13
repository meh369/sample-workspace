import datetime as dt
# t = datetime.time(5, 25, 1)
# print(t)
# print(datetime.time)
# print(datetime.time.min)
# print(datetime.time.max)
# print(datetime.time.resolution)
# today = datetime.date.today()
# print(today.timetuple())
'''try some finance analysis'''
import matplotlib.pyplot as plt 
from matplotlib import style
import pandas as pd 
import pandas_datareader.data as web 
style.use('ggplot')
import mplfinance as mpf

import matplotlib.dates as mdates

'''code for saving'''
# class Save_csv:
#     '''For saving file to csv'''
#     def __init__(self, df, name = "C:\\\\Users\mdevran\Documents\Sample-WorkSpace\Tesla.csv"):
#         self.df = df
#         self.name = name
        
#     def save(self):
#         return self.df.to_csv(self.name) 
    
#     def __str__(self):
#         return f'File {self.name[-9:]} is saved!!'

# class Data():
#     '''data for storing df'''
#     pass

# class Timestamp():
#     '''for time-stamping'''
#     pass
# date_start = Timestamp()
# date_end= Timestamp()

# tesla = Data()

# date_start.start = dt.datetime(2016, 1, 1)
# date_end.end =  dt.datetime(2020, 1, 1)

# tesla.file = web.DataReader('TSLA', 'yahoo', date_start.start, date_end.end)

# save = Save_csv(tesla.file)

# print(save.name)

## Save
# save.save()
# print(save)

class Read_file():
    '''Dataframe manupulations'''

    def __init__(self, file_url = 'C:\\Users\mdevran\Documents\Sample-WorkSpace\Tesla.csv', parse_date=True):
        self.name = file_url
        self.date = parse_date
        
    def read(self):
        '''read the file'''

        return pd.read_csv(self.name, parse_dates = self.date, index_col=0)

    def plot_ts(self):
        '''plot some graphs'''

        df = Read_file().read()
        df['Adj Close'].plot()
        df.plot()
        plt.show()
        plt.show()

    def ma(self, number):
        '''Show moving averages of adj close'''

        df = Read_file().read()
        return df['Adj Close'].rolling(window=number).mean() 

    def drop_na(self, df):
        return df.dropna()

    def ma_plot(self, df):
        '''plotting moving averages and volume bars'''

        ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
        ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1)

        ax1.plot(df.index, df['Adj Close'])
        ax1.plot(df.index, df['100_ma'])
        ax2.bar(df.index, df['Volume'])
        plt.show()

    def show_candle_sticks(self, df):
        '''convert date time to matplotlib readable date'''
        ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
        ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1)

        mpf.plot(df, type='candle', volume=True)
        plt.show()

    def resample(self, df):
        ohlc = df['Adj Close'].resample('10D').ohlc()
        ohlc['Volume'] = df['Volume'].resample('10D').sum()
        # ohlc.reset_index(inplace=True)
        return ohlc

    def __str__(self):
        return 'Reading file..wait a moment'

data = Read_file()
df = data.read()
# print(df.tail(9))

# data.plot_ts()

df['100_ma'] = data.ma(100)
# print(df.shape)

df_dropna = data.drop_na(df)
# print(df_dropna.shape)

# data.ma_plot(df_dropna)

df_ohlc = data.resample(df_dropna)
# print(df_ohlc.tail()) 

## plot candles 
# data.show_candle_sticks(df_ohlc)


        