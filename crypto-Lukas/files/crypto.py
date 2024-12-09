import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from binance.spot import Spot
import time
from datetime import datetime, timedelta
import ast
import matplotlib.dates as mdates
from datetime import datetime, timezone
from matplotlib.widgets import Button

coin = "BTCUSDT"

def check_if_positive(strPercent: str) -> str:
    if float(strPercent) >= 0:
        strPercent = "+" + strPercent
    return str(strPercent)

def costumise_axes(ax):
    ax.fill_between([], [], color='#1f77b4', alpha=0.1)
    ax.legend(loc='upper left', fontsize=10, frameon=True)
    ax.legend()

def checkColor(percent) -> str:
    return "green" if percent >= 0 else "red"

def on_button_clicked(event):
    global coin
    print(coin)
    if(coin == "BTCUSDT"):
      coin = "ETHUSDT"
      plt.close()
      BTCGraph("ETHUSDT")
      
    elif(coin =="ETHUSDT"):
      coin = "BTCUSDT"
      plt.close()
      BTCGraph("BTCUSDT")
      
def BTCGraph(coin:str):
    
    plt.style.use('dark_background')
    plt.rcParams['toolbar'] = 'None'
    fig, ax = plt.subplots()
    plt.subplots_adjust(bottom=0.2)
    button_width = 0.1  # Width of the button
    button_height = 0.075  # Height of the button
    button_ax = plt.axes([0.5 - button_width / 2, 0.05, button_width, button_height])  # Centered


    # Load the image once at the start
    if coin == "BTCUSDT":
      img = mpimg.imread("./crypto-Lukas/img/BTC.jpg")
      button = Button(button_ax, "ETH", color = "black")
      button.label.set_color("green")

    elif coin == "ETHUSDT":
      img = mpimg.imread("./crypto-Lukas/img/ETH.png")
      button = Button(button_ax, "ETH", color = "black")
      button.label.set_color("green")
    
    button.on_clicked(on_button_clicked)
    
  
    im_obj = ax.imshow(img, extent=[0, 1, 0, 1], aspect='auto', alpha=0.5, zorder=-1)
    
    line, = ax.plot([], [], label=coin + " price", color='blue', linestyle='-', linewidth=2, alpha=1, marker=0, markersize=7)

    fig.set_figwidth(15)
    fig.set_figheight(10)

    client = Spot()
    costumise_axes(ax)

    price_list = []
    percent = 0
    time_index = []

    fig.canvas.manager.full_screen_toggle()
    text_box = None

    while True:
        
        if text_box:
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

        percent = (100 * price_list[-1] / price_list[0]) - 100
        strPercent = round(percent, 2)      
        strPercent = str(strPercent)
        strPercent = check_if_positive(strPercent)

        line.set_data(time_objects, price_list)
        right_margin = timedelta(seconds=10)

        ax.set_xlim(time_objects[0], time_objects[-1] + right_margin)        
        ax.set_ylim(min(price_list) * 0.9999, max(price_list) * 1.00006)
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))

        current_xmin, current_xmax = ax.get_xlim()
        current_ymin, current_ymax = ax.get_ylim()
        
        extent = [
            current_xmin,  
            current_xmax,  
            current_ymin,  
            current_ymax   
        ]
        
        im_obj.set_extent(extent) 

        # Update text box
        props = dict(boxstyle='round', facecolor='none', edgecolor='none', alpha=0)
        text_box = ax.text(
            0.05, 0.05,
            f"{price}$ {strPercent}%", 
            transform=ax.transAxes, 
            color=checkColor(percent),
            fontsize=20, 
            verticalalignment='bottom',  
            bbox=props
        )
        plt.draw()
        plt.pause(1)

class BTC:
    def main():
        BTCGraph(coin)
    main()
