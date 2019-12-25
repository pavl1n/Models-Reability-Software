import tkinter as tk
import math

class Dzh_Moranda(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent
        self.init_ui()

    def init_ui(self):
        self.pack(fill=tk.BOTH, expand=1)
        acts = ["Число ошибок, первоначально находящихся в программе:", "Коэффициент пропорциональности:",
                'Количество ошибок спустя время:',
                "Время обнаружения i-ошибки:"]
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
        self.label = tk.Label(self, text=acts[3])
        self.label.pack(pady=10)
        self.entry3 = tk.Entry(self)
        self.entry3.pack(pady=1)
        self.button = tk.Button(self, text="Вывод результата", command=self.on_select)
        self.button.pack(pady=15)
        self.text = tk.Text(self, height=12, width=70, font='Arial 10')
        self.text.pack(pady=5)
        self.clear_button = tk.Button(self, text="Очистить поле", command=self.clear)
        self.clear_button.pack(pady=15)
        self.pack()

    def on_select(self):
        self.N = float(self.entry.get())
        self.C = float(self.entry1.get())
        self.i = float(self.entry2.get())
        self.t = float(self.entry3.get())
        self.lambdaa = self.C * (self.N - self.i + 1)
        self.P = self.lambdaa * math.exp(self.lambdaa * (-1) * self.t)
        self.text.insert(1.0, 'Функция плотности распределения времени обнаружения i-й'
                              ' ошибки, отсчитываемого от момента выявления: ' + str(self.P) + '\n')


    def clear(self):
        self.text.delete('1.0', tk.END)