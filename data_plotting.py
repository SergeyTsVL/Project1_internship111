import matplotlib.pyplot as plt
import pandas as pd

import logging
from colorama import Fore
import data_download as dd

import main as mn
from ta.momentum import RSIIndicator

def create_and_save_plot(data, ticker, period, filename=None):

    plt.figure(figsize=(10, 6))
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True)
    if 'Date' not in data:
        if pd.api.types.is_datetime64_any_dtype(data.index):
            dates = data.index.to_numpy()
            ax1.plot(dates, data['Close'].values, label='Close Price', color='red')
            ax1.plot(dates, data['Moving_Average'].values, label='Moving Average')
            # Построение тренда индикатора RSI
            ax2.plot(dates, dd.indicators_RSI(ticker, period), label='Indicator RSI')
            # Построение тренда индикатора MACD и линии сигнала
            ax3.plot(data.index, dd.indicators_MACD(ticker, period)['MACD'].values, label='MACD', color='red')
            ax3.plot(data.index, dd.indicators_MACD(ticker, period)['Signal Line'].values, label='Signal', color='green')
        else:
            print("Информация о дате отсутствует или не имеет распознаваемого формата.")
            return
    else:
        if not pd.api.types.is_datetime64_any_dtype(data['Date']):
            data['Date'] = pd.to_datetime(data['Date'])
        else:
            return None
        ax1.plot(data['Date'], data['Close'], label='Close Price', color='red')
        ax1.plot(data['Date'], data['Moving_Average'], label='Moving Average')
        # Построение тренда индикатора RSI
        ax2.plot(data['Date'], dd.indicators_RSI(ticker, period), label='Indicator RSI')
        # Построение тренда индикатора MACD и линии сигнала
        ax3.plot(data.index, dd.indicators_MACD(ticker, period)['MACD'].values, label="MACD", color='red')
        ax3.plot(data.index, dd.indicators_MACD(ticker, period)['Signal Line'].values, label='Signal', color='green')
    ax1.set_title(label=f"{ticker} Цена акций с течением времени", loc="center")
    ax2.set_title(label="Индекс относительной силы(RSI)", loc="center")
    ax3.set_title(label="Cхождение/расхождение скользящих средних(MACD)", loc="center")
    # Подписываем общую ось "х"
    plt.xlabel("Дата")
    # Подписываем "у" шкалы каждого из графиков
    ax1.set_ylabel('Цена')
    ax2.set_ylabel('RSI')
    ax3.set_ylabel('MACD')
    # Добавляем легенды на каждый график
    ax1.legend()
    ax2.legend()
    ax3.legend()
    # Добавляем сетку, для удобства определения значений
    ax1.grid(True)
    ax2.grid(True)
    ax3.grid(True)
    if filename is None:
        filename = f"{ticker}_{period}_stock_price_chart.png"
    else:
        return None
    plt.savefig(f"images/{filename}")
    print(f"График сохранен как {filename}")


def calculate_and_display_average_price(data):
    try:
        a = data['Close'].values()
        period_prices = sum(a) / len(a)
        print(f'Cреднее значение колонки "Close" за период составляет: {period_prices}')
        logging.info(f"Среднее значение за период {period_prices}")
    except BaseException as err:
        logging.error(f"Произошла ошибка {err} определения среднего значения за период!", exc_info=True)
        return 0


def notify_if_strong_fluctuations(data, threshold):
    a = data['Close'].values
    if float(max(a)) - float(min(a)) > threshold:
        print(Fore.RED + f"Превышено максимальное пороговое значения между максимальной и минимальной ценой закрытия!"
              + Fore.WHITE)


def export_data_to_csv(data, filename):

    df = pd.DataFrame(data)
    df.to_csv(f'CSV_file/{filename}', sep=',', index=False)

