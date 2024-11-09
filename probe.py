# import tkinter as tk
# from tkinter import simpledialog
# my_w = tk.Tk()
# my_w.geometry("410x360")
# my_w.title("www.plus2net.com")  # Adding a title
#
# my_i = simpledialog.askinteger("Input","Input an Integer",parent=my_w)
# print(my_i)
#
# my_w.mainloop()


# from tkinter import *
# from tkinter import simpledialog
#
# # Создание объекта TK (окна tkinter) [1](https://www.delftstack.com/howto/python-tkinter/tkinter-different-methods-of-the-simpledialog/)
# window = Tk()
# window.geometry("200x200")
# window.title("Deltstack")
#
# def intdialogbox():
#     # метод принимает целое число и возвращает целое число [1](https://www.delftstack.com/howto/python-tkinter/tkinter-different-methods-of-the-simpledialog/)
#     employee_age = simpledialog.askinteger("Input", "Enter your age", parent=window)
#     dialog_output = Label(window, text=f"Employee age is {employee_age}", font=("italic 12"))
#     dialog_output.pack(pady=20)
#
# dialog_btn = Button(window, text="dialog button", command=intdialogbox)
# dialog_btn.pack()
# window.mainloop()

import tkinter as tk


class TwoValueDialog:
    def __init__(self, parent):
        self.top = tk.Toplevel(parent)
        self.top.title("Enter two values")

        tk.Label(self.top, text="First value:").grid(row=0, column=0)
        tk.Label(self.top, text="Second value:").grid(row=1, column=0)

        self.entry1 = tk.Entry(self.top)
        self.entry2 = tk.Entry(self.top)

        self.entry1.grid(row=0, column=1)
        self.entry2.grid(row=1, column=1)

        tk.Button(self.top, text="OK", command=self.ok).grid(row=2, column=0, columnspan=2)

        self.values = None

    def ok(self):
        try:
            self.values = (float(self.entry1.get()), float(self.entry2.get()))
            self.top.destroy()
        except ValueError:
            print("Invalid input")

    def run(self):
        self.top.wait_window()
        return self.values


root = tk.Tk()
button = tk.Button(root, text="Get values",
                   command=lambda: print(TwoValueDialog(root).run()))
button.pack()
root.mainloop()
#
# import tkinter as tk
# from PIL import Image, ImageDraw, ImageTk
#
#
# class DrawingApp:
#     def __init__(self, root):
#         self.root = root
#         self.width = 800
#         self.height = 600
#         self.drawing_area = tk.Canvas(self.root, width=self.width, height=self.height)
#         self.drawing_area.pack()
#         self.setup()
#         self.old_x = None
#         self.old_y = None
#         self.line_width = 5
#         self.color = 'black'
#         self.eraser_on = False
#         self.shape = ''
#         self.start_x = None
#         self.start_y = None
#         self.end_x = None
#         self.end_y = None
#         self.image = Image.new('RGB', size=(self.width, self.height), color='white')
#         self.draw = ImageDraw.Draw(self.image)
#         self.photo = ImageTk.PhotoImage(self.image)
#         self.drawing_area.create_image(0, 0, image=self.photo, anchor=tk.NW)
#         self.drawing_area.tag_bind(self.photo, '<B1-Motion>', self.paint)
#         self.drawing_area.tag_bind(self.photo, '<ButtonRelease-1>', self.reset)
#         self.create_menu()
#
#     def create_menu(self):
#         menubar = tk.Menu(self.root)
#         self.root.config(menu=menubar)
#         filemenu = tk.Menu(menubar, tearoff=0)
#         menubar.add_cascade(label="File", menu=filemenu)
#         filemenu.add_command(label="New", command=self.new_canvas)
#         filemenu.add_separator()
#         filemenu.add_command(label="Exit", command=self.root.quit)
#
#     def new_canvas(self):
#         width = simpledialog.askinteger("Canvas Size", "Enter width")
#         height = simpledialog.askinteger("Canvas Size", "Enter height")
#
#         if width is not None and height is not None:
#             self.width = width
#             self.height = height
#
#             # Обновляем размеры холста
#             self.drawing_area.config(width=self.width, height=self.height)
#
#             # Создаем новый объект Image с новыми размерами
#             self.image = Image.new('RGB', size=(self.width, self.height), color='white')
#             self.draw = ImageDraw.Draw(self.image)
#             self.photo = ImageTk.PhotoImage(self.image)
#
#             # Обновляем изображение на холсте
#             self.drawing_area.delete(tk.ALL)
#             self.drawing_area.create_image(0, 0, image=self.photo, anchor=tk.NW)
#             self.drawing_area.tag_bind(self.photo, '<B1-Motion>', self.paint)
#             self.drawing_area.tag_bind(self.photo, '<ButtonRelease-1>', self.reset)
#
#     # Остальные методы остаются без изменений