import csv
import json
import sqlite3
import numpy as np
import matplotlib.pyplot as plt

def read_file_json(filepath: str):
    with open(filepath, "r") as file:
        return json.load(file)

'Q1: task1'
class GoldPrice:
    def __init__(self, date: str, buy: int, sell: int):
        self.date = date
        self.buy = buy
        self.sell = sell

    def __str__(self):
        return f'{self.date:<15}{self.buy:<15,}{self.sell:,}'

'Q1: task2'
def display_gold_table():
    print("Date                Buy           Sell\n" + "-" * 36)
    for item in gold_price:
        print(item)

'Q2: task1'
def save_lowest_buy_to_sqlite():
    conn = sqlite3.connect(file_db)
    cursor = conn.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS gold_price (date TEXT, buy INTEGER, sell INTEGER)")
    cursor.execute("DELETE FROM gold_price")

    lowest_buy = min(gold_price, key=lambda x: x.buy)

    cursor.execute("INSERT INTO gold_price(date, buy, sell) VALUES (?, ? , ? )", (lowest_buy.date, lowest_buy.buy, lowest_buy.sell))
    conn.commit()
    conn.close()

'Q2: task2'
def read_gold_price_from_db():
    conn = sqlite3.connect(file_db)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM gold_price")
    rows = cursor.fetchone()
    print(rows)

'Q3: task1'
def calculate_fluctuation():
     for item in gold_price:
         item.fluctuation = item.sell - item.buy

'Q3: task2'
def export_fluctuation_to_csv():
    calculate_fluctuation()
    with open(file_csv, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['date', 'buy', 'sell', 'fluctuation'])
        writer.writeheader()
        writer.writerows(vars(item) for item in gold_price)

'Q4: task1'
def read_file_csv():
    with open(file_csv, newline='') as csvfile:
        return list(csv.DictReader(csvfile))

'Q4: task2'
def highest_and_lowest_fluctuation_from_csv():
    data = read_file_csv()
    lowest_fluctuation_index = min(data, key=lambda x: int(x['buy']) - int(x['sell']))
    highest_fluctuation_index = max(data, key=lambda x: int(x['buy']) - int(x['sell']))

    lowest_fluctuation = int(lowest_fluctuation_index['buy']) - int(lowest_fluctuation_index['sell'])
    highest_fluctuation = int(highest_fluctuation_index['buy']) - int(highest_fluctuation_index['sell'])

    print(f"Highest Difference (Buy - Sell): {highest_fluctuation} on {highest_fluctuation_index['date']}")
    print(f"Lowest Difference (Buy - Sell): {lowest_fluctuation} on {lowest_fluctuation_index['date']}")

'Q5: task1'
def plot_sell_trend():
    date = [item.date for item in gold_price]
    buy = [item.buy for item in gold_price]
    sell = [item.sell for item in gold_price]

    plt.figure(figsize=(10, 5))
    plt.plot(date, sell, label="Sell", marker='o', color='r')
    plt.plot(date, buy, label="Buy", marker='s', color='b')
    plt.xticks(rotation=45)
    plt.title("Gold Buy/Sell Trend", fontsize=10)
    plt.xlabel('Date', fontsize=8)
    plt.ylabel('Price', fontsize=8)
    plt.grid()
    plt.legend()
    plt.tight_layout()
    
'Q5: task2'
    plt.savefig('sell_buy_trend.png')
    plt.show()


if __name__ == "__main__":
    file_json = 'gold_data.json'
    file_db = 'gold.db'
    file_csv = 'gold_report.csv'
    gold_price = [GoldPrice(date=item['date'], buy=item['buy'], sell=item['sell']) for item in read_file_json(file_json)]

    display_gold_table()
    print()
    save_lowest_buy_to_sqlite()
    read_gold_price_from_db()

    print()
    export_fluctuation_to_csv()
    highest_and_lowest_fluctuation_from_csv()
    plot_sell_trend()
