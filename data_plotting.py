import matplotlib.pyplot as plt
import pandas as pd

import logging
from colorama import Fore
import data_download as dd

import main as mn
from ta.momentum import RSIIndicator

def create_and_save_plot(data, ticker, period, filename=None):
    plt.figure(figsize=(10, 6))
    fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)

    if 'Date' not in data:
        if pd.api.types.is_datetime64_any_dtype(data.index):
            dates = data.index.to_numpy()
            ax1.plot(dates, data['Close'].values, label='Close Price')
            ax1.plot(dates, data['Moving_Average'].values, label='Moving Average')

            ax2.plot(dates, dd.indicators_RSI(ticker, period), label='Indicator RSI')
        else:
            print("Информация о дате отсутствует или не имеет распознаваемого формата.")
            return
    else:
        if not pd.api.types.is_datetime64_any_dtype(data['Date']):
            data['Date'] = pd.to_datetime(data['Date'])
        else:
            return None
        ax1.plot(data['Date'], data['Close'], label='Close Price')
        ax1.plot(data['Date'], data['Moving_Average'], label='Moving Average')

        ax2.plot(data['Date'], dd.indicators_RSI(ticker, period), label='Indicator RSI')
    plt.title(label=f"{ticker} Цена акций с течением времени", loc="center")

    plt.xlabel("Дата")
    ax1.set_ylabel('Цена')
    ax2.set_ylabel('RSI')
    # ax1.plt.ylabel("Цена")
    # ax2.ylabel("//////")

    plt.legend()
    plt.tight_layout(pad=1.5, w_pad=1.0, h_pad=1.0)
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

