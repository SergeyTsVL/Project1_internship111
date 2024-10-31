import tkinter

# Создание окна по умолчанию
root = tkinter.Tk()
root.title("Welcome to GeeksForGeeks")
root.geometry('700x500')

# Создание списка опций
options_list = ["Option 1", "Option 2", "Option 3", "Option 4"]

# Переменная для отслеживания выбранного варианта в OptionMenu
value_inside = tkinter.StringVar(root)

# Установка значения по умолчанию для переменной
value_inside.set("Select an Option")

# Создание виджета OptionMenu и передача ему созданного списка опций и переменной
question_menu = tkinter.OptionMenu(root, value_inside, *options_list)
question_menu.pack()

# Функция для печати отправленного варианта
def print_answers():
    print("Selected Option: {}".format(value_inside.get()))
    return None

# Кнопка отправки
submit_button = tkinter.Button(root, text='Submit', command=print_answers)
submit_button.pack()
root.mainloop()


