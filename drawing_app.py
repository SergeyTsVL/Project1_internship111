# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import colorchooser, filedialog, messagebox
from PIL import Image, ImageDraw
# from tkinter import *


ACTIVATION_CONTROL = 0
LIST_ACTIVATION_CONTROL = []

class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Рисовалка с сохранением в PNG")

        self.image = Image.new("RGB", (600, 400), "white")
        self.draw = ImageDraw.Draw(self.image)

        self.canvas = tk.Canvas(root, width=600, height=400, bg='white')
        self.canvas.pack()

        self.setup_ui()

        self.last_x, self.last_y = None, None
        self.pen_color = 'black'

        self.canvas.bind('<B1-Motion>', self.paint)
        self.canvas.bind('<ButtonRelease-1>', self.reset)


    def setup_ui(self):

        control_frame = tk.Frame(self.root)
        control_frame.pack(fill=tk.X)

        clear_button = tk.Button(control_frame, text="Очистить", command=self.clear_canvas)
        clear_button.pack(side=tk.LEFT)

        color_button = tk.Button(control_frame, text="Выбрать цвет", command=self.choose_color)
        color_button.pack(side=tk.LEFT)

        save_button = tk.Button(control_frame, text="Сохранить", command=self.save_image)
        save_button.pack(side=tk.LEFT)

        eraser_button = tk.Button(control_frame, text="Ластик", command=self.choose_color_eraser)
        eraser_button.pack(side=tk.LEFT)

        # # pipette_button =
        # self.canvas.bind('<Button-3>', self.pick_color)

        # Создание списка значений толщины
        options_list = [x for x in range(1, 11)]
        # Переменная для отслеживания выбранного варианта в OptionMenu
        self.value_inside = tk.StringVar()
        # Установка значения по умолчанию для переменной
        self.value_inside.set(options_list[0])
        # Создание виджета OptionMenu и передача ему созданного списка опций и переменной
        brush_size_scale = tk.OptionMenu(control_frame, self.value_inside, *options_list)
        brush_size_scale.pack(side=tk.LEFT)

    def paint(self, event):
        if self.last_x and self.last_y:
            self.canvas.create_line(self.last_x, self.last_y, event.x, event.y,
                                    width=int(self.value_inside.get()), fill=self.pen_color or
                                    LIST_ACTIVATION_CONTROL[-1], # Если self.pen_color будет None то цвет будет
                                    # последним элементом списка
                                    capstyle=tk.ROUND, smooth=tk.TRUE)
            self.draw.line([self.last_x, self.last_y, event.x, event.y], fill=self.pen_color or
                           LIST_ACTIVATION_CONTROL[-1],  # Если self.pen_color будет None то цвет будет
                                    # последним элементом списка
                           width=int(self.value_inside.get()))   # Необходимо было поставить int(

        self.last_x = event.x
        self.last_y = event.y

    def reset(self, event):
        self.last_x, self.last_y = None, None

    def clear_canvas(self):
        self.canvas.delete("all")
        self.image = Image.new("RGB", (600, 400), "white")
        self.draw = ImageDraw.Draw(self.image)

    # def pick_color(self):
    #     self.image.getpixel((x, self.pen_color))
    def choose_color(self):
        """
        В методе используем ACTIVATION_CONTROL как счетчик кликов на кнопку 'Ластик', а LIST_ACTIVATION_CONTROL
        используем как накопитель данных для запоминания какой цвет был последним
        """
        self.pen_color = colorchooser.askcolor(color=self.pen_color)[1]
        # Корректируем счетчик таким
        global ACTIVATION_CONTROL
        if self.pen_color != None:
            LIST_ACTIVATION_CONTROL.append(self.pen_color)
            ACTIVATION_CONTROL += 1
        else:
            None


    def choose_color_eraser(self):   # рализация работы ластика через список, при этом чтобы список постоянно сокращаем
        """
        В методе используем ACTIVATION_CONTROL как счетчик кликов на кнопку 'Ластик', а LIST_ACTIVATION_CONTROL
        используем как накопитель данных для запоминания какой цвет был последним.
        Конструкция if self.pen_color != None: определяет, что если при переходе в меню выбора цвета, не произошел выбор
        цвета то мы сохраняем в LIST_ACTIVATION_CONTROL последний выбранный цвет self.pen_color, иначе в список будет
        внесен None и придется перевыбирать цвет.
        При нажатии кнопки 'Ластик' происхоит смена цвета на "white", либо смена "white" на последний использованный
        цвет маркера.
        """
        global ACTIVATION_CONTROL
        # Реализация акивности и неактивности действия ластика, каждое четное нажатие включает ластик, нечетное - отключ
        if ACTIVATION_CONTROL % 2 == 0:
            # Ластик включается переводом self.pen_color на белый цвет
            if self.pen_color != None:
                try:
                    if LIST_ACTIVATION_CONTROL[-1] != self.pen_color:
                        LIST_ACTIVATION_CONTROL.append(self.pen_color)
                except:
                    self.pen_color = "white"
            else:
                None
            self.pen_color = "white"

        else:
            try:
                self.pen_color = LIST_ACTIVATION_CONTROL[-1]
            except:
                self.pen_color = 'black'
        ACTIVATION_CONTROL += 1


    def save_image(self):
        file_path = filedialog.asksaveasfilename(filetypes=[('PNG files', '*.png')])
        if file_path:
            if not file_path.endswith('.png'):
                file_path += '.png'
            else:
                None
            self.image.save(file_path)
            messagebox.showinfo("Информация", "Изображение успешно сохранено!")
        else:
            None


def main():
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()