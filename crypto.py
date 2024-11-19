import matplotlib.pyplot as plt
import numpy as np
from binance.spot import Spot
import time

# Initialize the Spot client
client = Spot()
counter = 0
price_list = []

# Get the current Bitcoin price
while counter < 10:
    btc_price = client.ticker_price("BTCUSDT")
    
    # Extract and print the price, converting it to float
    price = float(btc_price['price'])
    print(f"Current Bitcoin Price: {price}")
    price_list.append(price)
    
    time.sleep(1)
    counter += 1

# Prepare x-values
x_values = list(range(1, len(price_list) + 1))  # [1, 2, 3, ..., 10]

# Plot the data
plt.style.use('dark_background')
plt.plot(x_values, price_list, marker='o', label='Bitcoin Price')

# Customize plot
plt.xlim(0, 20)  # Set x-axis range
plt.ylim(0, 150000)  # Set y-axis range
plt.xlabel('Time (Index)')
plt.ylabel('Price (USDT)')
plt.title('Bitcoin Price Over Time')
plt.legend()

# Show the plot
plt.show()
