import matplotlib.pyplot as plt
import numpy as np
from binance.spot import Spot
import time
from datetime import datetime
import ast
import matplotlib.dates as mdates

# Initialize the Spot client (add API key if needed)
client = Spot()

# Initialize data lists
price_list = []
time_index = []


# Initialize the plot

plt.ion()  # Turn on interactive mode
plt.style.use('dark_background')
fig, ax = plt.subplots()
fig.set_figwidth(10)
fig.set_figheight(5)


ax.set_xlim(0, 20)  # Initial x-axis range
ax.set_xlabel('Time')
ax.set_ylabel('Price (USDT)')
ax.set_title('Bitcoin Price Over Time')

line, = ax.plot([], [],label='Bitcoin Price')
#line, = ax.plot_date([], [], marker='o', label='BTC Price', xdate=True)
ax.legend()
props = dict(boxstyle='round', facecolor='red', alpha=0.5)
text_box = ax.text(0.05, 0.95, "price", transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)


while True:
        text_box.remove()
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
        print(formatted_time)
        
        #print(formatted_time)

        btc_price = client.ticker_price("BTCUSDT")
        price = float(btc_price['price'])
        price_list.append(price)
        print(f"BTC Price = {price}")
        

        line.set_data(time_objects, price_list)
        
        ax.set_xlim(time_objects[0], time_objects[-1])
        #ax.set_ylim(min(price_list) * 0.4, max(price_list) * 1.05)
        ax.set_ylim(97000, 98000)
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
        props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
        text_box = ax.text(0.05, 0.95, price, transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props, backgroundcolor='red')
        #text_box.remove()
        plt.draw()
        plt.pause(1) 

        

