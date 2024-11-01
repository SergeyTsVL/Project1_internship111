# import tkinter

# Создание окна по умолчанию
# root = tkinter.Tk()
# root.title("Welcome to GeeksForGeeks")
# root.geometry('700x500')
#
# # Создание списка опций
# options_list = ["Option 1", "Option 2", "Option 3", "Option 4"]
#
# # Переменная для отслеживания выбранного варианта в OptionMenu
# value_inside = tkinter.StringVar(root)
#
# # Установка значения по умолчанию для переменной
# value_inside.set("Select an Option")
#
# # Создание виджета OptionMenu и передача ему созданного списка опций и переменной
# question_menu = tkinter.OptionMenu(root, value_inside, *options_list)
# question_menu.pack()
#
# # Функция для печати отправленного варианта
# def print_answers():
#     print("Selected Option: {}".format(value_inside.get()))
#     return None
#
# # Кнопка отправки
# submit_button = tkinter.Button(root, text='Submit', command=print_answers)
# submit_button.pack()
# root.mainloop()


# from tkinter import *
#
# root = Tk()
# root.geometry("600x600")
#
# def paint(event):
#     x1, y1, x2, y2 = (event.x-5), (event.y-5), (event.x+5), (event.y+5)
#     Colour = "#CB5E7F"
#     # get the selected width directly using variable.get()
#     w.create_line( x1, y1, x2, y2, fill=Colour, width=variable.get())
#
# w = Canvas(root, width=400, height=250, bg="white")
# w.bind("<B1-Motion>", paint)
#
# l = Label(root, text="Click and Drag to draw." )
# l.place(x=150, y=400)
# w.place(x=45, y=80)
#
# # create option menu for the line width
# options= ["10", "20", "30"]
# variable = StringVar(root)
# variable.set(options[0])
#
# menu= OptionMenu(root, variable, *options)
# menu.configure(bg="black", fg="white", font=('Arial', 14))
# menu.place(x=370, y=10)
#
# root.mainloop()


# import tkinter as tk
#
# def example_cget_usage():
#     root = tk.Tk()
#     root.title("Cget Example")
#
#     # Создаем несколько виджетов
#     label = tk.Label(root, text="Это пример использования cget()")
#     label.pack(pady=20)
#
#     entry = tk.Entry(root)
#     entry.pack(pady=10)
#
#     button = tk.Button(root, text="Кликните меня!")
#     button.pack(pady=10)
#
#     canvas = tk.Canvas(root, width=200, height=100, bg="white")
#     canvas.pack(pady=10)
#
#     # Примеры использования cget() с ключом
#     print("Текст кнопки:", button.cget("text"))
#     print("Цвет фона канваса:", canvas.cget("bg"))
#     print("Размер входного поля:", entry.cget("width"), "x", entry.cget("height"))
#
#     # Получаем несколько конфигураций одновременно
#     config = label.cget("fg", "font", "wraplength")
#     print("Фронт цвет, шрифт,.wraplength:", config)
#
#     # Проверяем наличие пользовательской конфигурации
#     if hasattr(button, "custom_config"):
#         print("Значение пользовательской конфигурации:", button.cget("custom_config"))
#     else:
#         print("Пользовательская конфурация не определена")
#
#     root.mainloop()
#
# if __name__ == "__main__":
#     example_cget_usage()
#
# from tkinter import *
#
# root = Tk()
#
# # Создаем список опций
# options = ["Option 1", "Option 2", "Option 3"]
#
# # Создаем связанную переменную
# var = StringVar(value=options[0])
#
# # Создаем OptionMenu
# option_menu = OptionMenu(root, var, *options)
# option_menu.pack()
#
# # Функция для вывода выбранного значения
# def print_selection():
#     # Получаем связанную переменную
#     selection_var = option_menu.cget("textvariable")
#     # Получаем выбранное значение
#     selected_value = selection_var.get()
#     print(f"Выбрано: {selected_value}")
#
# # Создаем кнопку для вызова функции
# button = Button(root, text="Показать выбор", command=print_selection)
# button.pack()
#
# root.mainloop()

