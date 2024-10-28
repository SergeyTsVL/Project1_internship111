import matplotlib.pyplot as plt
import pandas as pd

import logging
from colorama import Fore
import data_download as dd


def create_and_save_plot(data, ticker, period, filename=None, style_use=None):

    plt.figure(figsize=(20, 12))
    # Добавляем слили к таблицам
    plt.style.use(style_use)
    fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, sharex=True)
    plt.subplots_adjust(wspace=0.4, hspace=0.4) # Растояние между графиками, чтобы названия залазили на графики
    if 'Date' not in data:
        if pd.api.types.is_datetime64_any_dtype(data.index):
            dates = data.index.to_numpy()
            ax1.plot(dates, data['Close'].values, label='Close Price', color='red')
            ax1.plot(dates, data['Moving_Average'].values, label='Moving Average')
            # Построение тренда индикатора RSI
            ax2.plot(dates, dd.indicators_RSI(data), label='Indicator RSI')
            # Построение тренда индикатора MACD и линии сигнала
            ax3.plot(data.index, dd.indicators_MACD(data)['MACD'].values, label='MACD', color='red')
            ax3.plot(data.index, dd.indicators_MACD(data)['Signal Line'].values, label='Signal', color='green')
            # standard_deviation(data)
            ax4.plot(data.index, dd.standard_deviation(data)['Std_Dev'].values, label='Std_Dev', color='green')
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
        ax2.plot(data['Date'], dd.indicators_RSI(data), label='Indicator RSI')
        # Построение тренда индикатора MACD и линии сигнала
        ax3.plot(data.index, dd.indicators_MACD(data)['MACD'].values, label="MACD", color='red')
        ax3.plot(data.index, dd.indicators_MACD(data)['Signal Line'].values, label='Signal', color='green')

        ax4.plot(data.index, dd.standard_deviation(data)['Std_Dev'].values, label='Std_Dev', color='blue')

    ax1.set_title(label=f"{ticker} Цена акций с течением времени", loc="center")
    ax2.set_title(label="Индекс относительной силы(RSI)", loc="center")
    ax3.set_title(label="Cхождение/расхождение скользящих средних(MACD)", loc="center")
    ax4.set_title(label="Стандартное отклонения цены закрытия", loc="center")
    # Подписываем общую ось "х"
    plt.xlabel("Дата")
    # Подписываем "у" шкалы каждого из графиков
    ax1.set_ylabel('Цена')
    ax2.set_ylabel('RSI')
    ax3.set_ylabel('MACD')
    ax4.set_ylabel('Std_Dev')
    # Добавляем легенды на каждый график
    ax1.legend()
    # ax2.legend()
    ax3.legend()
    ax4.legend()
    # Добавляем сетку, для удобства определения значений
    ax1.grid(True)
    ax2.grid(True)
    ax3.grid(True)
    ax4.grid(True)
    # ax4.set_ylim([-10, 10])
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

