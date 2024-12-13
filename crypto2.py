import matplotlib.pyplot as plt
import numpy as np
from binance.spot import Spot
from binance.client import Client
import time
from datetime import datetime, timedelta
import ast
import matplotlib.dates as mdates
from time import sleep
from decimal import Decimal

client = Spot()
client2 = Client()

price_list = []
time_index = []
price_list_eth = []

plt.ion() 
plt.style.use('dark_background')
plt.rcParams['toolbar'] = 'None'
fig, (ax1, ax2) = plt.subplots(2)
fig.set_figwidth(10)
fig.set_figheight(5)
#figManager = plt.get_current_fig_manager()
#figManager.full_screen_toggle()

#ax.set_xlim(0, 20)  # Initial x-axis range
ax1.set_xlabel('Time')
ax1.set_ylabel('Price (USDT)')
ax1.set_title('Bitcoin Price Over Time')


line, = ax1.plot([], [],
                label='Bitcoin Price',
                color='gold',    
                linestyle='-',      
                linewidth=2,       
                alpha=0.85,        
                marker='o',         
                markersize=2)  

line2, = ax2.plot([], [],
                label='Ethereum',
                color='blue',   
                linestyle='-',      
                linewidth=2,        
                alpha=0.85,         
                marker='o',         
                markersize=2)  

ax1.fill_between([], [], color='#1f77b4', alpha=0.1)
ax1.legend(loc='upper left', fontsize=10, frameon=True)

ax2.fill_between([], [], color='#1f77b4', alpha=0.1)
ax2.legend(loc='upper left', fontsize=10, frameon=True)
ax1.legend()
ax2.legend()
props = dict(boxstyle='round', facecolor='red', alpha=0.5)
props1 = dict(boxstyle='round', facecolor='red', alpha=0.5)
props2 = dict(boxstyle='round', facecolor='red', alpha=0.5)
text_box = ax1.text(0.05, 0.95, "price", transform=ax1.transAxes, fontsize=14, verticalalignment='top', bbox=props)
text_box2 = ax2.text(0.05, 0.95, "price", transform=ax2.transAxes, fontsize=14, verticalalignment='top', bbox=props)

text_box1_percent = ax1.text(0.4, 0.95, "price", transform=ax1.transAxes, fontsize=14, verticalalignment='top', bbox=props)
text_box2_percent = ax2.text(0.4, 0.95, "price", transform=ax2.transAxes, fontsize=14, verticalalignment='top', bbox=props)

#end_time = datetime.now()  # Current time
#start_time = end_time - timedelta(hours=24)  # 24 hours ago

# Convert times to milliseconds
##start_time_ms = int(start_time.timestamp() * 1000)
#end_time_ms = int(end_time.timestamp() * 1000)

# Fetch historical klines for the last 24 hours
#interval = Client.KLINE_INTERVAL_1HOUR
#klines = client2.get_historical_klines("BTCUSDT", interval, start_time_ms, end_time_ms)
#print(klines)
#print(klines[0][0])
#for klines in klines:
    ##print(klines[4])
   #price_list = klines[4]

#print(price_list)





while True:
        plt.gca().yaxis.get_major_formatter().set_useOffset(False)
        text_box.remove()
        text_box2.remove()
        text_box1_percent.remove()
        text_box2_percent.remove()
        

        date = client.time()
        data = str(date)
        data_dict = ast.literal_eval(data)
        server_time = data_dict['serverTime']
        milliseconds = server_time                            #TIME X-ACHSE                                                   
        seconds = milliseconds / 1000
        normal_time = datetime.utcfromtimestamp(seconds)
        formatted_time = normal_time.strftime('%H:%M:%S')
        time_index.append(formatted_time)
        time_objects = [datetime.strptime(i, '%H:%M:%S') for i in time_index]

        btc_price = client.ticker_price("BTCUSDT")
       
        price = float(btc_price['price'])
        price_list.append(price)

        eth_price = client.ticker_price("ETHUSDT")
        price_eth = float(eth_price['price'])
        price_list_eth.append(price_eth)

        text_box1_percent = ax1.text(0.2, 0.95, "20s change")
        text_box2_percent = ax2.text(0.2, 0.95, "20s change")
          
        
        
        try:
                percent_eth_int = (((price_list_eth[-1] - price_list_eth[-60]) / price_list_eth[-60]) * 100)
                percent_btc_int = (((price_list[-1] - price_list[-60]) / price_list[-60]) * 100)

                percent_eth = str(round((((price_list_eth[-1] - price_list_eth[-60]) / price_list_eth[-60]) * 100), 2)) + "% per min"
                percent_btc = str(round((((price_list[-1] - price_list[-60]) / price_list[-60]) * 100), 2)) + "% per min"
                print(percent_btc)
                print(percent_eth)

                if percent_btc_int < 0:
                        props2 = dict(boxstyle='round', facecolor='red', alpha=0.5) 
                        
                elif  percent_btc_int >= 0:
                        props2 = dict(boxstyle='round', facecolor='green', alpha=0.5) 
                        percent_btc = "+" + percent_btc 
                if percent_eth_int < 0:
                        props1 = dict(boxstyle='round', facecolor='red', alpha=0.5) 
                elif  percent_eth_int >= 0:
                        props1 = dict(boxstyle='round', facecolor='green', alpha=0.5)         

                text_box1_percent = ax1.text(0.2, 0.95, percent_btc, transform=ax1.transAxes, fontsize=14, verticalalignment='top', bbox=props2)
                text_box2_percent = ax2.text(0.2, 0.95, percent_eth, transform=ax2.transAxes, fontsize=14, verticalalignment='top', bbox=props1)
        
        except IndexError:
                pass
        
        line.set_data(time_objects, price_list)
        line2.set_data(time_objects, price_list_eth)
        right_margin = timedelta(seconds=10)  

        ax1.set_xlim(time_objects[0], time_objects[-1] + right_margin)
        ax2.set_xlim(time_objects[0], time_objects[-1] + right_margin)
        
        ax1.set_ylim((min(price_list) * 0.9999, max(price_list) * 1.00006))
        ax2.set_ylim((min(price_list_eth) * 0.9999, max(price_list_eth) * 1.00006))
        ax1.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
        ax2.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
        
        text_box = ax1.text(0.05, 0.95, str(price) + "$", transform=ax1.transAxes, fontsize=14, verticalalignment='top', bbox=props2, backgroundcolor='none')
        text_box2 = ax2.text(0.05, 0.95, str(price_eth) + "$", transform=ax2.transAxes, fontsize=14, verticalalignment='top', bbox=props1, backgroundcolor='none')

        if len(price_list) > 100:
                price_list = price_list[-100:]
                price_list_eth = price_list_eth[-100:]
                time_index = time_index[-100:]

        plt.draw()
        plt.pause(1)
        