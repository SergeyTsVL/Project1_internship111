# # Загружаем данные по акции
# from ta.momentum import RSIIndicator
# import yfinance as yf
#
# ticker = yf.Ticker('AAPL')
# data = ticker.history(period='1mo')
#
# # Создаем объект RSI
# rsi = RSIIndicator(data["Close"])
#
# # Добавляем RSI к датафрейму
# data["RSI"] = rsi.rsi()
#
# # Отображаем результаты
# print(data["RSI"].tail())

# import matplotlib.pyplot as plt
# import numpy as np
#
# x = [0, 5, 9, 10, 15]
# y = [0, 1, 2, 3, 4]
#
# plt.plot(x, y)
# plt.xticks(np.arange(min(x), max(x) + 10, 1.0))  # изменяем шаг делений на оси X
# plt.show()
# ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
# import matplotlib.pyplot as plt
# import numpy as np
#
# # Create some mock data
# t = np.arange(0.01, 10.0, 0.01)
# data1 = np.exp(t)
# data2 = np.sin(2 * np.pi * t)
#
# fig, ax1 = plt.subplots()
#
# color = 'tab:red'
# ax1.set_xlabel('time (s)')
# ax1.set_ylabel('exp', color=color)
# ax1.plot(t, data1, color=color)
# ax1.tick_params(axis='y', labelcolor=color)
#
# ax2 = ax1.twinx()  # instantiate a second Axes that shares the same x-axis
#
# color = 'tab:blue'
# ax2.set_ylabel('sin', color=color)  # we already handled the x-label with ax1
# ax2.plot(t, data2, color=color)
# ax2.tick_params(axis='y', labelcolor=color)
#
# fig.tight_layout()  # otherwise the right y-label is slightly clipped
# plt.show()
# ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
# import matplotlib.pyplot as plt
# import numpy as np
#
# # Создаём некоторые фиктивные данные
# t = np.arange(0.01, 10.0, 0.01)
# data1 = np.exp(t)
# data2 = np.sin(2 * np.pi * t)
#
# # Создаём первую ось
# fig, ax1 = plt.subplots()
# color = 'tab:red'
# ax1.set_xlabel('time (s)')
# ax1.set_ylabel('exp', color=color)
# ax1.plot(t, data1, color=color)
# ax1.tick_params(axis='y', labelcolor=color)
#
# # Создаём вторую ось, которая разделяет ту же ось X
# ax2 = ax1.twinx()
# color = 'tab:blue'
# ax2.set_ylabel('sin', color=color)
# ax2.plot(t, data2, color=color)
# ax2.tick_params(axis='y', labelcolor=color)
#
# fig.tight_layout()
# plt.show()
# *******************************************************************
# import numpy as np
# import matplotlib.pyplot as plt
#
# # Исходные данные испольуземые в примере:
# x = np.linspace(0, 10, 100)
# y1 = np.exp(x)  # Экспоненциальная зависимость
# y2 = np.log(x + 1)  # Логарифмическая зависимость
#
# fig, ax1 = plt.subplots()
#
# # Первая ось Y и соответствующая метка
# ax1.plot(x, y1, 'g-')
# ax1.set_ylabel('Экспоненциальная зависимость', color='g')
#
# # Добавление дополнительной оси Y и соответствующей метки
# ax2 = ax1.twinx()
# ax2.plot(x, y2, 'b-')
# ax2.set_ylabel('Логарифмическая зависимость', color='b')
#
# plt.show()
# ***************************************************************
# import matplotlib.pyplot as plt
# import numpy as np
#
#
# values_1 = range(1,51)
# log_values_1 = -np.log(values_1)
#
# values_2 = range(1,101)
# log_values_2 = -np.log(values_2)
#
# fig, axs = plt.subplots(1, 2, figsize=(10,20) )
#
# for i in range(50):
#     axs[0].axhline(log_values_1[i], color="blue")
# for i in range(100):
#     axs[1].axhline(log_values_2[i], color="red")
# axs[0].set_yticks(log_values_1[::-1],[str(v) for v in values_1[::-1]])
# axs[0].yaxis.set_ticks_position("left")
# axs[0].yaxis.set_label_position("left")
#
# axs[1].set_xticks([])
# axs[1].yaxis.set_ticks_position("right")
# axs[1].yaxis.set_label_position("right")
# axs[1].set_yticks(log_values_2[::-1],[str(v) for v in values_2[::-1]] )
# axs[0].get_shared_y_axes().join(axs[0], axs[1])
# axs[0].autoscale()
# plt.show()
# **********************************************************************
# import matplotlib.pyplot as plt
# import numpy as np
# x=np.linspace(0, 100)
# a=x*0.01
# b=np.sqrt(x)
# fig, ax = plt.subplots()
# ax1 = ax.twinx()
# ax.plot(x,a,color='r')
# ax1.plot(x,b,color='b')
# ax.set_ylabel('Для красного графика')
# ax1.set_ylabel('Для синего графика')
# x_t = [10**5]
# y_t = [10**3]
# x_t_2 = [10**5]
# y_t_2 = [10**3]
# t_h = [0]
#
# h = 1
# fig, (ax1,ax2) = plt.subplots(2, 1, sharex=True)
# ax1.plot(t_h, x_t_2, label= 'x(t)')
# ax2.plot(t_h, y_t_2, label = 'y(t)')
# ax1.legend()
# ax2.legend()
# plt.show()
# *************************************************************************
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 1000)
y1 = x * 0.1
y2 = np.sin(x)

fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
ax1.plot(x, y1, 'b-')
ax2.plot(x, y2, 'r-')

ax1.set_ylabel('First y-axis')
ax2.set_ylabel('Second y-axis')
ax2.set_xlabel('X-axis')

plt.tight_layout(pad=15, w_pad=10.0, h_pad=5.0,
                 rect=[0.05, 0.05, 0.05, 0.055],
                 )

plt.show()

# import matplotlib.pyplot as plt
# import numpy as np
# # Шаг 2: Создание данных
# x = np.linspace(0, 10, 100)
# y1 = x * 0.1
# y2 = np.sin(x)
# # Шаг 3: Создание основной оси и добавление первого графика
# fig, ax1 = plt.subplots()
# ax1.plot(x, y1, 'b-', label='Первый набор данных')
# ax1.set_xlabel('X-ось')
# ax1.set_ylabel('Первая ось Y', color='b')
# ax1.tick_params(axis='y', labelcolor='b')
# # Шаг 4: Создание дополнительной оси и добавление второго графика
# ax2 = ax1.twinx()  # Создаем дополнительную ось, которая делит одну ось Y
# ax2.plot(x, y2, 'r-', label='Второй набор данных')
# ax2.set_ylabel('Вторая ось Y', color='r')
# ax2.tick_params(axis='y', labelcolor='r')
# # Шаг 5: Дополнительные настройки
# plt.title('Два разных масштаба на одной оси')
# plt.legend()
# plt.tight_layout(pad=1.08)  # Для корректного размещения графиков

# plt.show()


# import matplotlib.pyplot as plt
# import numpy as np
#
# x = np.linspace(0, 10, 100)
# y1 = x * 0.1
# y2 = np.sin(x)
#
# fig, ax1 = plt.subplots()
# ax1.plot(x, y1, 'b-', label='Первый набор данных')
# ax1.set_xlabel('X-ось')
# ax1.set_ylabel('Первая ось Y', color='b')
#
# ax2 = ax1.twinx()
# ax2.plot(x, y2, 'r-', label='Второй набор данных')
# ax2.set_ylabel('Вторая ось Y', color='r')
#
# plt.title('Два разных масштаба на одной оси')
# plt.legend()
#
# # Настройка tight_layout
# plt.tight_layout(pad=1.5, w_pad=1.0, h_pad=1.0,
#                  rect=[0.05, 0.05, 0.95, 0.95],
#                  )
#
# plt.show()

