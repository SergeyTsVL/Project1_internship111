# import tkinter as tk
#
# border_effects = {
#     "flat": tk.FLAT,
#     "sunken": tk.SUNKEN,
#     "raised": tk.RAISED,
#     "groove": tk.GROOVE,
#     "ridge": tk.RIDGE,
# }
#
# window = tk.Tk()
#
# for relief_name, relief in border_effects.items():
#     frame = tk.Frame(master=window, relief=relief, borderwidth=5)
#     frame.pack(side=tk.LEFT)
#     label = tk.Label(master=frame, text=relief_name)
#     label.pack()
#
# window.mainloop()

# import tkinter as tk
#
# window = tk.Tk()
#
# frame1 = tk.Frame(master=window, width=100, height=100, bg="red")
# frame1.pack()
#
# frame2 = tk.Frame(master=window, width=50, height=50, bg="yellow")
# frame2.pack()
#
# frame3 = tk.Frame(master=window, width=25, height=25, bg="blue")
# frame3.pack()
#
# window.mainloop()

# import tkinter
# from tkinter import *
# from tkinter import messagebox
#
# top = Tk()
# top.geometry("300x150")
# def click():
#     messagebox.showinfo("Hello", "Green Button clicked")
# a = Button(top, text="yellow", activeforeground="yellow", activebackground="orange", pady=10)
# b = Button(top, text="Blue", activeforeground="blue", activebackground="orange", pady=10)
# # adding click function to the below button
# c = Button(top, text="Green", command=click, activeforeground = "green", activebackground="orange", pady=10)
# d = Button(top, text="red", activeforeground="yellow", activebackground="orange", pady=10)
#
# a.pack(side = LEFT)
# b.pack(side = RIGHT)
# c.pack(side = TOP)
# d.pack(side = BOTTOM)
# top.mainloop()

import tkinter as tk


class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.pen_color = "#FF0000"  # Красный

        self.color_label = tk.Label(root, text=f"Текущий цвет: {self.pen_color}", fg=self.pen_color)
        self.color_label.pack()

        self.button = tk.Button(root, text="Изменить цвет", command=self.change_color)
        self.button.pack()

    def change_color(self):
        self.pen_color = "#00FF00"  # Зеленый
        self.color_label.config(text=f"Текущий цвет: {self.pen_color}", fg=self.pen_color)


root = tk.Tk()
app = DrawingApp(root)
root.mainloop()