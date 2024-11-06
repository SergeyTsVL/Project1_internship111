import tkinter as tk
from tkinter import filedialog, colorchooser, messagebox

class ImageEditor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Редактор изображений")
        self.geometry("400x300")

        self.image_label = None

        self.open_button = tk.Button(self, text="Открыть изображение", command=self.open_image)
        self.open_button.pack(pady=10)

        self.save_button = tk.Button(self, text="Сохранить изображение", command=self.save_image)
        self.save_button.pack()

        self.color_button = tk.Button(self, text="Изменить цвет", command=self.change_color)
        self.color_button.pack()

        # Биндинг события Ctrl+S
        self.bind('<Control-s>', self.save_image)

    def open_image(self):
        filename = filedialog.askopenfilename(filetypes=[("Image Files", ".png .jpg .jpeg")])
        if filename:
            self.image_label = tk.PhotoImage(file=filename)
            label = tk.Label(self, image=self.image_label)
            label.image = self.image_label
            label.pack()

    def save_image(self, event=None):
        if self.image_label:
            filename = filedialog.asksaveasfilename(defaultextension=".png",
                                                    filetypes=[("PNG Image", "*.png"), ("JPEG Image", "*.jpg *.jpeg")])
            if filename:
                try:
                    self.image_label.save(filename)
                    messagebox.showinfo("Success", "Изображение успешно сохранено!")
                except Exception as e:
                    messagebox.showerror("Error", f"Не удалось сохранить изображение: {str(e)}")
        else:
            messagebox.showwarning("Warning", "Пожалуйста, открыть изображение перед его сохранением.")

    def change_color(self):
        color = colorchooser.askcolor()
        if color[1]:  # Проверяем, был ли выбран цвет
            self.image_label = tk.PhotoImage(file="path_to_your_image.png").convert_alpha()
            self.image_label.putalpha(color[2])  # Задаем прозрачность
            self.image_label.save("temp.png")
            self.image_label = tk.PhotoImage(file="temp.png")
            self.image_label.save("final.png")
            messagebox.showinfo("Success", "Цвет изображения изменен!")

if __name__ == "__main__":
    app = ImageEditor()
    app.mainloop()