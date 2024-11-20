import matplotlib.pyplot as plt
import numpy as np
from binance.spot import Spot
import time
import ast

# Initialize the Spot client
client = Spot()
price = client.klines("BTCUSDT", "3d", limit=1)
date = client.time()

data = str(date)
data_dict = ast.literal_eval(data)
server_time = data_dict['serverTime']

milliseconds = server_time

seconds = milliseconds / 1000
normal_time = datetime.utcfromtimestamp(seconds)
formatted_time = normal_time.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]  

print("Normal Time:", formatted_time)
for i in price:
    price2 = i

plt.style.use('dark_background')

x = np.array([1, 2, 3, 2])
print(price2)
y = np.array(price2)
plt.plot(y, marker = 'o')
plt.show()
