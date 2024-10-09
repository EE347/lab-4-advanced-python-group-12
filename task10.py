import csv
import matplotlib.pyplot as plt
from datetime import datetime

dates = []
prices = {'META': [], 'AAPL': [], 'AMZN': [], 'NFLX': [], 'NVDA': [], 'GOOGL': []}
colors = {'META': 'blue', 'AAPL': 'gray', 'AMZN': 'black', 'NFLX': 'red', 'NVDA': 'green', 'GOOGL': 'orange'}
percentage_changes = {}

with open("task9.csv", "r") as file:
 reader = csv.reader(file)
 next(reader)
 for row in reader:
  dates.append(datetime.strptime(row[0], '%d/%m/%Y'))

  for i, stock in enumerate(prices.keys(), start=1):
   prices[stock].append(float(row[i]))

for stock in prices:
 initial_price = prices[stock][0]
 final_price = prices[stock][-1]
 prices[stock] = [(price / initial_price - 1) * 100 for price in prices[stock]]

 percentage_changes[stock] = (final_price / initial_price - 1) * 100

for stock, stock_prices in prices.items():
 label_with_percentage = f"{stock}: {percentage_changes[stock]:.2f}%"
 plt.plot(dates, stock_prices, label=label_with_percentage, color=colors[stock])

plt.title("Stock Prices Over Time (percentage change)")
plt.xlabel("Date")
plt.ylabel("Percentage Change (%)")
plt.legend()
plt.grid(True)
plt.gcf().autofmt_xdate()
plt.show()

