import csv
import matplotlib.pyplot as plt
from datetime import datetime

dates = []
prices = {'META': [], 'AAPL': [], 'AMZN': [], 'NFLX': [], 'NVDA': [], 'GOOGL': []}

with open("task9.csv", "r") as file:
 reader = csv.reader(file)
 next(reader)
 for row in reader:
  dates.append(datetime.strptime(row[0], '%d/%m/%Y'))

  for i, stock in enumerate(prices.keys(), start=1):
   prices[stock].append(float(row[i]))

for stock, stock_prices in prices.items():
 plt.plot(dates, stock_prices, label=stock)

plt.title("Stock Prices Over Time")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.legend()
plt.grid(True)
plt.gcf().autofmt_xdate()
plt.show()

