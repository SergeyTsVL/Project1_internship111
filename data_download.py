# -*- coding: utf-8 -*-
import yfinance as yf
from ta.momentum import RSIIndicator
import pandas as pd
from ta.trend import MACD
import ta

def fetch_stock_data(ticker, period='1mo'):
    """
    Метод определяет за какой период сделать выборку из "DataFrame" даных об акции, в "data" передает все данные по
    акциям. Допустимые периоды: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max с начала года, максимум
    Допустимые интервалы: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
    """
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    return data


def add_moving_average(data, window_size=5):
    """
    Метод определяет цену закрытия по акциям, берет в data в колонке "Close".
    "rolling(window=window_size).mean()" обозначает расчёт скользящего среднего с указанным размером окна (window_size).
    :param data:
    :param window_size:
    :return:
    """
    data['Moving_Average'] = data['Close'].rolling(window=window_size).mean()
    return data

# class Indicators():

def indicators_RSI(ticker, period):

    ticker = yf.Ticker(ticker)           # Загружаем данные по акции
    data = ticker.history(period=period)
    rsi = RSIIndicator(data["Close"])    # Создаем объект RSI
    data["RSI"] = rsi.rsi()              # Добавляем RSI к датафрейму
    RSI_indic = data["RSI"].values
    return RSI_indic




# Функция для расчета MACD
def indicators_MACD(ticker, period):
    # Загружаем данные по акции
    ticker = yf.Ticker(ticker)
    data = ticker.history(period=period)

    # Вычисляем EMA для короткого и длинного периодов
    ema_short = data['Close'].ewm(span=12, adjust=False).mean()
    ema_long = data['Close'].ewm(span=26, adjust=False).mean()

    # Вычисляем MACD линию
    macd_line = ema_short - ema_long

    # Вычисляем сигнальную линию
    signal_line = macd_line.ewm(span=9, adjust=False).mean()

    # Добавляем результаты к датафрейму
    data['MACD'] = macd_line
    data['Signal Line'] = signal_line

    return data
