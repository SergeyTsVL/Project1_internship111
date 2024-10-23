import logging
from datetime import datetime
import data_download as dd
import data_plotting as dplt
import yfinance as yf




def main():
    print("Добро пожаловать в инструмент получения и построения графиков биржевых данных.")
    print("Вот несколько примеров биржевых тикеров, которые вы можете рассмотреть: AAPL (Apple Inc), "
          "GOOGL (Alphabet Inc), MSFT (Microsoft Corporation), AMZN (Amazon.com Inc), TSLA (Tesla Inc).")
    print("Общие периоды времени для данных о запасах включают: 1д, 5д, 1мес, 3мес, 6мес, 1г, 2г, 5г, 10л, "
          "с начала года, макс.")

    ticker = input("Введите тикер акции, (по умолчанию AAPL): ") or 'AAPL'
    period = input("Введите период для данных, (по умолчанию False и переход на задание периода вручную): ") or False
    period = period if period != False else None
    stock = yf.Ticker(ticker)
    data = stock.history(period)

    if period == None:
        start = input("Введите дату начала периода в формате ГГГГ-ДД-ММ, (по умолчанию 2022-01-03): ") or '2022-01-03'
        end = input("Введите дату окончания периода в формате ГГГГ-ДД-ММ, (по умолчанию 2022-01-10): ") or '2023-01-10'
        interval = input("Введите интервал, например, 1s, 1m, 1h, 1d, 1wk, 1mo (по умолчанию 1d): ") or '1d'
        period = f'{start}_&_{end}'
        stock = yf.Ticker(ticker)
        data = stock.history(start=start, end=end, interval=interval)
    else:
        period = period

    threshold = float(input("Установите максимальное пороговое значение цены закрытияб (по умолчанию 20): ") or 20)

    # Fetch stock data
    stock_data = dd.fetch_stock_data(data)

    # Создаем csv файл с именем как дата и время создания
    now = datetime.now().strftime("%H.%M.%S___%d.%m.%Y")
    filename = f"{now}.csv"

    # Пороговые значения
    dplt.notify_if_strong_fluctuations(stock_data, threshold)

    # Add moving average to the data
    stock_data = dd.add_moving_average(stock_data)

    # Plot the data
    dplt.create_and_save_plot(stock_data, ticker, period)

    # Средняя цена закрытия
    dplt.calculate_and_display_average_price(data=stock_data)

    # Вывод данных в CSV файл
    dplt.export_data_to_csv(stock_data, filename)

    # Выводы индикаторов RSI и MACD
    dd.indicators_RSI(data)
    dd.indicators_MACD(data)

if __name__ == "__main__":

    logging.basicConfig(level=logging.INFO, filemode="w", filename="main.log",
                        format="%(asctime)s | %(levelname)s | %(message)s")
    main()
