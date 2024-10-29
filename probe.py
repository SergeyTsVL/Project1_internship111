# import numpy as np
# from ipywidgets import interact
# import ipywidgets as widgets
# from matplotlib import pyplot as plt
#
#
# def plot_func(freq):
#     plt.figure()
#     x = np.linspace(0, 2 * np.pi, 400)
#     y = np.sin(x * freq)
#     plt.plot(x, y)
#     plt.show()
#
#
#
# interact(plot_func, freq=widgets.FloatSlider(value=7.5, min=1, max=10, step=0.5));

# *****************************************************************

# from matplotlib.widgets import Button
# from matplotlib import pyplot as plt
# import numpy as np
#
# fig, ax = plt.subplots()
# scatter = ax.scatter(np.random.rand(10), np.random.rand(10))
#
# button_ax = plt.axes([0.7, 0.05, 0.1, 0.075])
# button = Button(button_ax, 'Add')
#
#
# def add_point(event):
#     new_point = np.random.rand(2)
#     scatter.set_offsets(np.concatenate([scatter.get_offsets(), [new_point]]))
#     plt.draw()
#
#
# button.on_clicked(add_point)
#
# plt.show()

# *****************************************************************
# nums = [2,6, 7,11,15]
# # print(nums[0])
# # print(len(nums))
# target = 9
# for i in range(len(nums)):
#     s = nums[0] + nums[i]
#     if s == target:
#         print(i)
# # for i in range(len(nums)):
# #
# #     print(nums[i])

import plotly.graph_objects as go

# Данные для графика
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]

# Создание графика
fig = go.Figure(data=go.Scatter(x=x, y=y, mode='lines+markers'))

# Добавление заголовка и подписей осей
fig.update_layout(title='Интерактивный график',
                  xaxis_title='Ось X',
                  yaxis_title='Ось Y')

# Отображение графика
fig.show()






