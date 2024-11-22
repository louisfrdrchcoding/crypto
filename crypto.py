import matplotlib.pyplot as plt
import numpy as np
from binance.spot import Spot
from matplotlib.animation import FuncAnimation
import datetime

client = Spot()
y_values = []
plt.style.use('dark_background')
plt.xlabel('Time (Index)')
plt.ylabel('Price (USDT)')
plt.title('Bitcoin Price Over Time')
time = []

class Counter:

    def setCounter(self, counter: int):
        self._counter = counter

    def getCounter(self)->int:
        return self._counter

c = Counter()
c.setCounter(0)

def update_btc_price(i):

    if c.getCounter() == 0:
        time.append((datetime.datetime.now().strftime("%M")))
    elif c.getCounter() == 10:
        time.append((datetime.datetime.now().strftime("%M")))
        c.setCounter(1)
    else:
        c.setCounter(c.getCounter()+1)

    btc_price = client.ticker_price("BTCUSDT")
        
    price = float(btc_price['price'])
    y_values.append(price)

    x_values = time
    plt.cla()
    plt.plot(x_values ,y_values, marker='s', label='Bitcoin Price')
  

ani = FuncAnimation(plt.gcf(), update_btc_price, interval=300)
plt.show()
