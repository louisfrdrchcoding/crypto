import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from binance.spot import Spot
import time
from datetime import datetime, timedelta
import ast
import matplotlib.dates as mdates
from datetime import datetime, timezone
from PIL import Image

def check_if_positive(strPercent:str)->str:

  if float(strPercent) >= 0:
    strPercent = "+"+strPercent

  return str(strPercent)

def costumise_axes(ax):

  ax.fill_between([], [], color='#1f77b4', alpha=0.1)
  ax.legend(loc='upper left', fontsize=10, frameon=True)
  
  ax.legend()

def checkColor(percent)->str:
    if percent >= 0:
      return "green"
    else:
      return "red"

def BTCGraph(coin: str):

    plt.style.use('dark_background')
    plt.rcParams['toolbar'] = 'None'
    fig, ax = plt.subplots()
    
    line, = ax.plot([], [],
                    
                    label=coin+" price",
                    color='blue',    # Professional blue color
                    linestyle='-',      # Solid line
                    linewidth=2,        # Moderate width
                    alpha=0.85,         # Slight transparency
                    marker='o',         # Highlight individual points
                    markersize=5) 

    

    fig.set_figwidth(10)
    fig.set_figheight(5)

    client = Spot()
    costumise_axes(ax)

    price_list = []
    percent = 0
    time_index = []

    props = dict(boxstyle='round', facecolor='green', alpha=0)
    text_box = ax.text(0.05, 0.95, "price", transform=ax.transAxes, fontsize=14, verticalalignment='bottom', bbox=props)

    while True:

            text_box.remove()
            date = client.time()
            data = str(date)
            data_dict = ast.literal_eval(data)
            server_time = data_dict['serverTime']
            milliseconds = server_time                                                
            seconds = milliseconds / 1000
            normal_time = datetime.fromtimestamp(seconds, tz=timezone.utc)
            formatted_time = normal_time.strftime('%H:%M:%S')
            time_index.append(formatted_time)
            time_objects = [datetime.strptime(i, '%H:%M:%S') for i in time_index]

            btc_price = client.ticker_price(coin)
            price = float(btc_price['price'])
            price_list.append(price)

            percent = (100*price_list[-1]/price_list[0])-100
            strPercent = round(percent, 2)      
            strPercent = str(strPercent)
            strPercent = check_if_positive(strPercent)
      
            line.set_data(time_objects, price_list)
            right_margin = timedelta(seconds=10)  # Add 10 seconds to the right edge

            ax.set_xlim(time_objects[0], time_objects[-1] + right_margin)        
            ax.set_ylim(min(price_list) * 0.9999, max(price_list) * 1.00006)
            ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
            img = mpimg.imread("files/10540.jpg")  # Load the image once at the top
            extent = [
              time_objects[0],  # x_min
              time_objects[-1] + right_margin,  # x_max
              min(price_list) * 0.9999,  # y_min
              max(price_list) * 1.00006   # y_max
            ]
            ax.imshow(img, extent=extent, aspect='auto', alpha = 1, zorder=0)
            plt.savefig('output.png', transparent=True, bbox_inches='tight', dpi=300)


            props = dict(boxstyle='round', facecolor='none', edgecolor='none', alpha=0)
            text_box = ax.text(
                0.05, 0.05,
                f"{price}$ {strPercent}%", 
                transform=ax.transAxes, 
                color = checkColor(percent),
                fontsize=13, 
                verticalalignment='bottom',  # Align text box to the bottom
                bbox=props
            )
            plt.draw()
            plt.pause(1) 
       
class BTC():

  def main():

    BTCGraph("ETHUSDT")

  main()