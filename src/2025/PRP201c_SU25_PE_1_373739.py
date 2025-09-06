import csv
import json
import matplotlib.pyplot as plt

def read_file_json(filepath: str):
    with open(filepath, "r") as file:
        return json.load(file)

'Q1'
class ExchangeRate:
    def __init__(self, date: str, USD: float, EUR: float, JPY: float, CNY: float):
        self.date = date
        self.USD = USD
        self.EUR = EUR
        self.JPY = JPY
        self.CNY = CNY

    def __str__(self):
        return f"{self.date}    {self.USD:.2f}  {self.EUR:.2f}  {self.JPY:.2f}  {self.CNY:.2f}"

def display_exchange_table():
    print('Date    USD    EUR  JPY    CNY')
    for item in exchange_rate:
        print(item)

'Q2'
def find_usd_extremes():

    lowest_usd_rate = min(exchange_rate, key=lambda x: x.USD)
    highest_usd_rate = max(exchange_rate, key=lambda x: x.USD)

    print(f"Highest USD: {highest_usd_rate.USD} on {highest_usd_rate.date}")
    print(f"Lowest USD: {lowest_usd_rate.USD} on {lowest_usd_rate.date}")
    
'Q3'
def calculate_usd_change_percent():
    lowest_date = min(exchange_rate, key=lambda x: x.date)
    highest_date = max(exchange_rate, key=lambda x: x.date)

    first = lowest_date.USD
    last = highest_date.USD
    formula = ((last - first) / first) * 100

    print(f"USD change by {formula:.2f}% from {lowest_date.date} to {highest_date.date}")

'Q4'
def plot_usd_trend():
    date = [item.date for item in exchange_rate]
    usd = [item.USD for item in exchange_rate]

    plt.figure(figsize=(6, 5))
    plt.plot(date, usd, marker='o', color='b')
    plt.xticks(rotation=45)
    plt.title("USD Exchange Rate Over Time", fontsize=10)
    plt.xlabel('Date', fontsize=8)
    plt.ylabel('USD Rate', fontsize=8)
    plt.tight_layout()

    plt.savefig('sell_buy_trend.png')
    plt.show()

'Q5'
def save_usd_fluctuation_report():
    rate1, rate2 = max(zip(exchange_rate, exchange_rate[1:]), key=lambda x: abs(x[1].USD - x[0].USD))
    fluctuation = abs(rate1.USD - rate2.USD)

    with open(file_csv, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['Date', 'USD Fluctuation'])
        writer.writeheader()
        writer.writerow({'Date': rate2.date, 'USD Fluctuation': fluctuation})


if __name__ == '__main__':
    file_json = 'exchange_rates.json'
    file_csv = 'report.csv'
    exchange_rate = [ExchangeRate(**item) for item in read_file_json(file_json)]

    display_exchange_table()
    print()
    find_usd_extremes()
    print()
    calculate_usd_change_percent()
    plot_usd_trend()

    save_usd_fluctuation_report()
