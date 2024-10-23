import yfinance as yf
from datetime import datetime, timezone

gold = yf.Ticker("AAPL")

start = input("Введите дату начала периода в формате ГГГГ-ДД-ММ, например, 2022-01-03: ") or '2022-01-03'
end = input("Введите дату окончания периода в формате ГГГГ-ДД-ММ, например, 2022-01-10: ") or '2022-01-10'
interval = input(
    "Введите интервал, например, 1s, 1m, 1h, 1d, 1wk, 1mo (не забывайте про правила ввода yfinance): ") or '1d'
period = f'start={start}, end={end}, interval={interval}'
print(period)
# data = gold.history(interval='1d', start='2018-01-03', end='2022-01-10')
data = gold.history(period)
print(data)
