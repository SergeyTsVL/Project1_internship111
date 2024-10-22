import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Загружаем данные по акции
ticker = yf.Ticker("AAPL")
data = ticker.history(period="1y")


# Функция для расчета MACD
def calculate_macd(data, short_window=12, long_window=26, signal_window=9):
    # Вычисляем EMA для короткого и длинного периодов
    ema_short = data['Close'].ewm(span=short_window, adjust=False).mean()
    ema_long = data['Close'].ewm(span=long_window, adjust=False).mean()

    # Вычисляем MACD линию
    macd_line = ema_short - ema_long

    # Вычисляем сигнальную линию
    signal_line = macd_line.ewm(span=signal_window, adjust=False).mean()

    return macd_line, signal_line


# Расчет MACD
macd_line, signal_line = calculate_macd(data)

# Добавляем результаты к датафрейму
data['MACD'] = macd_line
data['Signal Line'] = signal_line

# Визуализация
plt.figure(figsize=(12, 6))
plt.plot(data.index, data['Close'], label='Price', alpha=0.5)
plt.plot(data.index, data['MACD'], label='MACD', color='red')
plt.plot(data.index, data['Signal Line'], label='Signal', color='green')
plt.title('AAPL Price and MACD Indicator')
plt.xlabel('Date')
plt.ylabel('Price/MACD')
plt.legend()
plt.grid(True)
plt.show()

# Проверка пересечений
for i in range(1, len(data)):
    if data['MACD'].iloc[i - 1] < data['Signal Line'].iloc[i - 1] and data['MACD'].iloc[i] > data['Signal Line'].iloc[i]:
        print(f'Бычий сигнал на {data.index[i]}')
    elif data['MACD'].iloc[i - 1] > data['Signal Line'].iloc[i - 1] and data['MACD'].iloc[i] < data['Signal Line'].iloc[i]:
        print(f'Mедвежий сигнал на {data.index[i]}')