import csv
import json
import sqlite3
import matplotlib.pyplot as plt

def read_file_json(filename):
    with open(filename) as json_file:
        return json.load(json_file)

'Q1'
def info_weather():
    latitude = weather['latitude']
    longitude = weather['longitude']
    elevation = weather['elevation']
    timezone = weather['timezone']
    print(f"Q1:\nLatitude: {latitude}\nlongitude: {longitude}\nelevation: {elevation}\ntimezone: {timezone}\n")

'Q2'
def max_fluctuation():
    max_index = max(range(len(max_temp)), key=lambda i: max_temp[i] - min_temp[i])
    print(f"Q2:\nDate:{date_weather[max_index]} \nValue:{max_temp[max_index] - min_temp[max_index]:.2f}\n")

'Q3'
def cold_day():
    arr_cold_day = [{
        'date': date_weather[i],
        'max_temp': max_temp[i],
        'min_temp': min_temp[i]
    } for i in range(len(date_weather)) if max_temp[i] < 15]

    formatted_list = '\n'.join(str({'date': item['date'], 'max_temp': item['max_temp']}) for item in arr_cold_day)
    print(f"Q3:\nCold Day:\n{formatted_list}\n")
    return arr_cold_day

'Q4'
def export_cold_day_to_csv():
    dict_cold_day = cold_day()

    with open(file_csv, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['date', 'max_temp', 'min_temp'])
        writer.writeheader()
        writer.writerows(dict_cold_day)

'Q5'
def weather_db():
    conn = sqlite3.connect(file_db)
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS weather_forecast (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        date TEXT,
                        max_temp REAL,
                        min_temp REAL
    )''')

    cursor.execute('''DELETE FROM weather_forecast''')

    arr_day = [{
        'date': date_weather[i],
        'max_temp': max_temp[i],
        'min_temp': min_temp[i],
        'fluctuation': round(max_temp[i] - min_temp[i], 2)
    } for i in range(len(date_weather))]

    print(f'Q4:\nCold Day:\n{arr_day}\n')
    conn.commit()
    conn.close()

'Q8'
def plot_temperature_trends():
    plt.figure(figsize=(10, 5))
    plt.plot(date_weather, max_temp, label='Max Temperature', marker='o')
    plt.plot(date_weather, min_temp, label='Min Temperature', marker='o')
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.title('Temperature Trends Over 14 Days')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    file_json = 'berlin_14day_weather.json'
    file_csv = 'cold_days.csv'
    file_db = 'weather.db'
    weather = read_file_json(file_json)
    date_weather = weather['daily']['time']
    max_temp = weather['daily']['temperature_2m_max']
    min_temp = weather['daily']['temperature_2m_min']

    info_weather()
    max_fluctuation()
    export_cold_day_to_csv()
    weather_db()
    plot_temperature_trends()
