import tkinter as tk

class ColorPickerApp:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(self.master, width=400, height=300)
        self.canvas.pack()

        # Связываем правую кнопку мыши с методом pick_color
        self.canvas.bind('<Button-3>', self.pick_color)

    def pick_color(self, event):
        x = event.x
        y = event.y
        color = self.canvas.cget('bg')  # Получаем цвет фона холста
        print(f"Выбрано цвет: {color}")

root = tk.Tk()
app = ColorPickerApp(root)
root.mainloop()