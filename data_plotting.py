import matplotlib.pyplot as plt
import pandas as pd

import logging
from colorama import Fore
import data_download as dd

import main as mn
from ta.momentum import RSIIndicator

def create_and_save_plot(data, ticker, period, filename=None):
    plt.figure(figsize=(10, 6))
    if 'Date' not in data:
        if pd.api.types.is_datetime64_any_dtype(data.index):
            dates = data.index.to_numpy()
            plt.plot(dates, data['Close'].values, label='Close Price')
            plt.plot(dates, data['Moving_Average'].values, label='Moving Average')

            plt.plot(dates, dd.indicators_RSI(ticker, period), label='Indicator RSI')
        else:
            print("Информация о дате отсутствует или не имеет распознаваемого формата.")
            return
    else:
        if not pd.api.types.is_datetime64_any_dtype(data['Date']):
            data['Date'] = pd.to_datetime(data['Date'])
        else:
            return None
        plt.plot(data['Date'], data['Close'], label='Close Price')
        plt.plot(data['Date'], data['Moving_Average'], label='Moving Average')

        plt.plot(data['Date'], dd.indicators_RSI(ticker, period), label='Indicator RSI')
    plt.title(f"{ticker} Цена акций с течением времени")
    plt.xlabel("Дата")
    plt.ylabel("Цена")
    plt.legend()
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

