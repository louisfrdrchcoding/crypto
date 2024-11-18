import matplotlib.pyplot as plt
import numpy as np
from binance.spot import Spot
from datetime import datetime
import ast
import re

client = Spot()
price = client.klines("BTCUSDT", "0.5h", limit=1)
date = client.time()

data = str(date)
data_dict = ast.literal_eval(data)
server_time = data_dict['serverTime']

milliseconds = server_time

seconds = milliseconds / 1000
normal_time = datetime.utcfromtimestamp(seconds)
formatted_time = normal_time.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]  

print("Normal Time:", formatted_time)
print(price)

#fig, ax = plt.subplots()
#ax.plot(x, y)
#plt.show()
