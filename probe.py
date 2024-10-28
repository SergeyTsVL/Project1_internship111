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

# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
#
# # Генерируем случайные данные о цене за 30 дней
# np.random.seed(42)
# prices = np.random.normal(100, 10, size=30)
#
# # Создаем DataFrame
# df = pd.DataFrame({'Date': pd.date_range(start='2023-01-01', periods=30),
#                    'Price': prices})
#
# # Расчет стандартного отклонения с окном в 7 дней
# df['Std_Dev'] = df['Price'].rolling(window=7).std()
# print(df['Std_Dev'])
# # Построение графика
# plt.figure(figsize=(12, 6))
#
# # График цены
# plt.plot(df['Date'], df['Price'], label='Цена', color='blue')
#
# # График стандартного отклонения
# plt.fill_between(df['Date'],
#                  df['Price'] + df['Std_Dev'],
#                  df['Price'] - df['Std_Dev'],
#                  alpha=0.3, label='Стандартное отклонение', color='blue')
#
# plt.title('Цена и стандартное отклонение')
# plt.xlabel('Дата')
# plt.ylabel('Цена')
# plt.legend()
# plt.grid(True)
# plt.show()
# # print(fill_between(df['Date'], df['Price'] + df['Std_Dev'], df['Price'] - df['Std_Dev'], alpha=0.3, label='Стандартное отклонение', color='blue'))


# print('У вас есть три коробки: в одной только яблоки, в другой только апельсины, а в третьей смешаны и яблоки, и '
#       'апельсины.')
# print('Все коробки промаркированы неправильно, и ни одна из этикеток не соответствует фактическому содержимому. ')
#
# a = input('Выверите коробку (например с надписью: яблоки, апельсины, яблоки и апельсины): ')
# b = input('Выверите фрукт который вы достали из коробки (например: яблоко или апельсин: ')
#
# if a == 'яблоки' and b == 'яблоко':
#     print('На коробках неправильные надписи, "яблоко" не может лежать в коробке "яблоки" --> значит в коробке "яблоки" '
#           'лежат яблоки и апельсины')
#     print('Так как надписи все неверные в коробке "апельсины" --> лежат яблоки, коробке "яблоки и апельсины" --> лежат '
#           'апельсины')
#     print("Ответ:")
#     print('Коробка "яблоки" --> лежат яблоки и апельсины')
#     print('Коробка "апельсины" --> лежат яблоки')
#     print('Коробка "яблоки и апельсины" --> лежат апельсины')
# else:
#     None
# if a == 'яблоки и апельсины' and b == 'яблоко':
#     print("В коробке 'яблоки и апельсины' лежать только яблоки")
#     print('Так как надписи все неверные в коробке "апельсины" --> лежат яблоки и апельсины, коробке "яблоки" --> лежат '
#           'апельсины')
#     print("Ответ:")
#     print('Коробка "яблоки" --> лежат апельсины')
#     print('Коробка "апельсины" --> лежат яблоки и апельсины')
#     print('Коробка "яблоки и апельсины" --> лежат яблоки')
# else:
#     None
# if a == 'яблоки и апельсины' and b == 'апельсин':
#     print("В коробке 'яблоки и апельсины' лежать только апельсины")
#     print('Так как надписи все неверные в коробке "апельсины" --> лежат яблоки, коробке "яблоки" --> лежат яблоки и '
#           'апельсины')
#     print("Ответ:")
#     print('Коробка "яблоки" --> лежат яблоки и апельсины')
#     print('Коробка "апельсины" --> лежат яблоки')
#     print('Коробка "яблоки и апельсины" --> лежат апельсины')
# else:
#     None
# if a == 'апельсины' and b == 'апельсин':
#     print('На коробках неправильные надписи, "апельсин" не может лежать в коробке "апельсины" --> значит в коробке '
#           '"апельсины" лежат яблоки и апельсины')
#     print('Так как надписи все неверные в коробке "яблоки и апельсины" --> лежат яблоки, коробке "яблоки" --> лежат '
#           'апельсины')
#     print("Ответ:")
#     print('Коробка "яблоки" --> лежат апельсины')
#     print('Коробка "апельсины" --> лежат яблоки и апельсины')
#     print('Коробка "яблоки и апельсины" --> лежат яблоки')
# else:
#     None






# if a == 'яблоко':
#     print()

import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

# Получаем данные о ценах закрытия Apple Inc. за последний год
ticker = yf.Ticker("AAPL")
data = ticker.history(period="1y")

# Выбираем только цену закрытия
data['Close'] = data['Close']

# Расчет средней цены
mean_close = data['Close'].mean()

# Расчет стандартного отклонения
std_deviation = np.std(data['Close'])

# Расчет индикатора стандартного отклонения
data['ATR'] = (data['High'] - data['Low']) / 2  # Простой ATR
data['ATR_14'] = data['ATR'].rolling(window=14).mean()  # Сглаживание ATR
data['STD_Close'] = (data['Close'] - mean_close) / std_deviation

print(f"Средняя цена за период: {mean_close:.2f}")
print(f"Стандартное отклонение цены закрытия за период: {std_deviation:.2f}")

# Создаем график
plt.figure(figsize=(12, 6))

# Нарисуем график цены закрытия и индикатора стандартного отклонения
plt.plot(data.index, data['Close'], label='Цена закрытия', linewidth=1)
plt.plot(data.index, data['STD_Close'] * std_deviation + mean_close, color='r', linestyle='-', label=f'Индикатор стандартного отклонения')

# Добавляем линию средней цены
plt.axhline(y=mean_close, color='g', linestyle='--', label=f'Средняя цена: {mean_close:.2f}')

# Настройка осей и заголовков
plt.title('Цены закрытия Apple Inc. за последний год с индикатором стандартного отклонения')
plt.xlabel('Дата')
plt.ylabel('Цена закрытия')

# Добавляем легенду и сетку
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)

# Отображение графика
plt.tight_layout()
plt.show()

print(f"Максимальное значение индикатора стандартного отклонения: {data['STD_Close'].max():.4f}")
print(f"Минимальное значение индикатора стандартного отклонения: {data['STD_Close'].min():.4f}")
