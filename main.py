import logging
from datetime import datetime
import data_download as dd
import data_plotting as dplt



def main():
    print("Добро пожаловать в инструмент получения и построения графиков биржевых данных.")
    print("Вот несколько примеров биржевых тикеров, которые вы можете рассмотреть: AAPL (Apple Inc), GOOGL (Alphabet Inc), MSFT (Microsoft Corporation), AMZN (Amazon.com Inc), TSLA (Tesla Inc).")
    print("Общие периоды времени для данных о запасах включают: 1д, 5д, 1мес, 3мес, 6мес, 1г, 2г, 5г, 10л, с начала года, макс.")

    ticker = input("Введите тикер акции (например, «AAPL» для Apple Inc): ")
    period = input("Введите период для данных (например, '1mo', '1y' для одного месяца, года): ")
    threshold = float(input("Установите максимальное пороговое значение цены закрытия: "))


    # Создаем csv файл с именем как дата и время создания
    now = datetime.now().strftime("%H.%M.%S___%d.%m.%Y")
    filename = f"{now}.csv"

    # Fetch stock data
    stock_data = dd.fetch_stock_data(ticker, period)

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


    dd.indicators_RSI(ticker, period)

    dd.indicators_MACD(ticker, period)

if __name__ == "__main__":

    logging.basicConfig(level=logging.INFO, filemode="w", filename="main.log",
                        format="%(asctime)s | %(levelname)s | %(message)s")
    main()
