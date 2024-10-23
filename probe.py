# import yfinance as yf
# from datetime import datetime, timezone
#
# gold = yf.Ticker("AAPL")
#
#
# data = gold.history(interval='1h', start='2018-01-03', end='2022-01-10')
# print(data)

# start = input("Введите дату начала периода в формате ГГГГ-ДД-ММ, например, 2022-01-03: ")
# end = input("Введите дату окончания периода в формате ГГГГ-ДД-ММ, например, 2022-01-10: ")
# interval = input("Введите интервал, например, 1s, 1m, 1h, 1d, 1wk, 1mo (не забывайте про правила ввода yfinance): ")
# period = f'start={start}, end={end}, interval={interval}'
# print(period)

a = input("Введите дату начала периода в формате ГГГГ-ДД-ММ, например, 2022-01-03: ") or 0
a = a if a != 0 else None
print(a)
# if a == '\n' or a is None or a == None:2

#     print(5)

# number = int(input('Type an integer: ') or 0)
# number = number if number != 0 else None
# print(number)

