import tkinter as tk

class Lipov(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent
        self.init_ui()

    def init_ui(self):
        self.pack(fill=tk.BOTH, expand=1)
        acts = ["Количество тестов:", "Общее количество внесенных ошибок:",
                'Первоначальное число ошибок в программе:',
                "Число найденных собственных ошибок:","Число обнаруженных к моменту оценки искусственных ошибок:"]
        self.label = tk.Label(self, text = acts[0])
        self.label.pack(pady = 10)
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
        self.label = tk.Label(self, text=acts[3])
        self.label.pack(pady=10)
        self.entry3 = tk.Entry(self)
        self.entry3.pack(pady=1)
        self.label = tk.Label(self, text=acts[4])
        self.label.pack(pady=10)
        self.entry4 = tk.Entry(self)
        self.entry4.pack(pady=1)
        self.button = tk.Button(self, text="Вывод результата", command=self.on_select)
        self.button.pack(pady = 15)
        self.text = tk.Text(self, height=8, width=75, font='Arial 10')
        self.text.pack(pady=5)
        self.clear_button = tk.Button(self, text="Очистить поле", command=self.clear)
        self.clear_button.pack(pady=15)
        self.pack()

    def on_select(self):
        self.m = float(self.entry.get())
        self.S = float(self.entry1.get())
        self.N = float(self.entry2.get())
        self.n = float(self.entry3.get())
        self.V = float(self.entry4.get())
        self.q = (self.n + self.V) / self.n;
        self.text.insert(1.0, 'Вероятность обнаружения n собственных и V внесенных ошибок: ' + str(self.toFixed((self.m / (self.n + self.V)) * (self.q ** (self.n + self.V)) * ((1 - self.q) ** (self.m - self.n - self.V)) * (
                    (self.N / self.n) * (self.S / self.V) / ((self.N + self.S) / (self.n + self.V))))) + '\n')


    def toFixed(self, numObj, digits=4):
        return f"{numObj:.{digits}f}"

    def clear(self):
        self.text.delete('1.0', tk.END)