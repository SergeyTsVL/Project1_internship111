# import yfinance as yf
# from datetime import datetime, timezone
#
# gold = yf.Ticker("AAPL")
#
# start = input("Введите дату начала периода в формате ГГГГ-ДД-ММ, например, 2022-01-03: ") or '2022-01-03'
# end = input("Введите дату окончания периода в формате ГГГГ-ДД-ММ, например, 2022-01-10: ") or '2022-01-10'
# interval = input(
#     "Введите интервал, например, 1s, 1m, 1h, 1d, 1wk, 1mo (не забывайте про правила ввода yfinance): ") or '1d'
# period = f'start={start}, end={end}, interval={interval}'
# print(period)
# # data = gold.history(interval='1d', start='2018-01-03', end='2022-01-10')
# data = gold.history(period)
# print(data)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Генерируем случайные данные о цене за 30 дней
np.random.seed(42)
prices = np.random.normal(100, 10, size=30)

# Создаем DataFrame
df = pd.DataFrame({'Date': pd.date_range(start='2023-01-01', periods=30),
                   'Price': prices})

# Расчет стандартного отклонения с окном в 7 дней
df['Std_Dev'] = df['Price'].rolling(window=7).std()
print(df['Std_Dev'])
# Построение графика
plt.figure(figsize=(12, 6))

# График цены
plt.plot(df['Date'], df['Price'], label='Цена', color='blue')

# График стандартного отклонения
plt.fill_between(df['Date'],
                 df['Price'] + df['Std_Dev'],
                 df['Price'] - df['Std_Dev'],
                 alpha=0.3, label='Стандартное отклонение', color='blue')

plt.title('Цена и стандартное отклонение')
plt.xlabel('Дата')
plt.ylabel('Цена')
plt.legend()
plt.grid(True)
plt.show()
# print(fill_between(df['Date'], df['Price'] + df['Std_Dev'], df['Price'] - df['Std_Dev'], alpha=0.3, label='Стандартное отклонение', color='blue'))
