# Загружаем данные по акции
from ta.momentum import RSIIndicator
import yfinance as yf

ticker = yf.Ticker('AAPL')
data = ticker.history(period='1mo')

# Создаем объект RSI
rsi = RSIIndicator(data["Close"])

# Добавляем RSI к датафрейму
data["RSI"] = rsi.rsi()

# Отображаем результаты
print(data["RSI"].tail())