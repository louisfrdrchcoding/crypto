import matplotlib.pyplot as plt
import numpy as np
from binance.spot import Spot
from datetime import datetime
import re

client = Spot()
data = client.klines("BTCUSDT", "1h", limit=1)
date = client.time()

print(date)

seconds1 = re.search(r"\+", date).group()

#for i in data:
 #   print(i)


milliseconds = seconds1

    # Convert milliseconds to seconds
seconds = milliseconds / 1000
    # Convert to a datetime object
normal_time = datetime.utcfromtimestamp(seconds)
    # Format the datetime object to a readable string
formatted_time = normal_time.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]  # Exclude last 3 digits of microseconds

# Example usage
print("Normal Time:", formatted_time)

#fig, ax = plt.subplots()
#ax.plot(x, y)
#plt.show()
