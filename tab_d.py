import tkinter as tk

class Mills(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent
        self.init_ui()

    def init_ui(self):
        self.pack(fill=tk.BOTH, expand=1)
        acts = ["Количество искусственно внесенных ошибок:", "Число собственных найденных ошибок:",
                'Число обнаруженных к моменту оценки искусственных ошибок:']
        self.label = tk.Label(self, text=acts[0])
        self.label.pack(pady=10)
        self.entry = tk.Entry(self)
        self.entry.pack(pady=1)
        self.label = tk.Label(self, text=acts[1])
        self.label.pack(pady=10)
        self.entry1 = tk.Entry(self)
        self.entry1.pack(pady=1)
        self.label = tk.Label(self, text=acts[2])
        self.label.pack(pady=10)
        self.entry2 = tk.Entry(self)
        self.entry2.pack(pady=1)
        self.button = tk.Button(self, text="Вывод результата", command=self.on_select)
        self.button.pack(pady=15)
        self.text = tk.Text(self, height=15, width=50, font='Arial 10')
        self.text.pack(pady=5)
        self.clear_button = tk.Button(self, text="Очистить поле", command=self.clear)
        self.clear_button.pack(pady=15)
        self.pack()

    def on_select(self):
        self.S = float(self.entry.get())
        self.n = float(self.entry1.get())
        self.V = float(self.entry2.get())
        self.N = (self.S * self.n) / self.V
        self.text.insert(1.0, 'Первоначальное число ошибок в программе равно: ' + str(int(self.N)) + '\n')


    def clear(self):
        self.text.delete('1.0', tk.END)