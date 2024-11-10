# import tkinter as tk
#
# # создание объекта холста
# canvas = tk.Canvas(width=500, height=500)
# canvas.pack()
#
# # создание объекта прямоугольника
# rectangle = canvas.create_rectangle(50, 50, 150, 150, fill='blue')
#
# # получение координат объекта прямоугольника
# coords = canvas.coords(rectangle)
# print(coords)

import tkinter as tk
root = tk.Tk()
def motion(event):
    x, y = event.x, event.y
    print('{}, {}'.format(x, y))
root.bind('<Motion>', motion)
root.mainloop()