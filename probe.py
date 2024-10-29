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
nums = [2,7,11,15]
target = 9
# for i in len(nums):
#     s = nums[0] + nums[i]
#     if s == target:
#         print(i)
for i in len(nums):
    print(nums[i])


