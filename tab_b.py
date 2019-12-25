import tkinter as tk

class Shuman(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent
        self.init_ui()


    def init_ui(self):
        self.pack(fill=tk.BOTH, expand=1)
        acts = ["Командных строк в программе:", "Строк содержащих ошибку:",
                'Дней работы:', "Ошибок за время работы:", "Коэффициент пропорциональности:"]
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
        self.label = tk.Label(self, text=acts[4])
        self.label.pack(pady=10)
        self.entry4 = tk.Entry(self)
        self.entry4.pack(pady=1)
        self.button = tk.Button(self, text="Вывод результата", command=self.on_select)
        self.button.pack(pady=15)
        self.text = tk.Text(self, height=10, width=80, font='Arial 10')
        self.text.pack(pady=5)
        self.clear_button = tk.Button(self, text="Очистить поле", command=self.clear)
        self.clear_button.pack(pady=15)
        self.pack()


    def on_select(self):
        self.s = float(self.entry.get())
        self.c_s = float(self.entry1.get())
        self.d = float(self.entry2.get())
        self.x = float(self.entry3.get())
        self.c = float(self.entry4.get())
        self.ec = (1 / self.s)
        self.er = (self.c_s/self.s)-self.ec
        self.tcp = 1/(self.c*self.er)
        self.lambdaa = self.c * self.er
        self.text.insert(1.0, 'Ошибок в расчёте на одну команду в машинном языке: ' + str(self.ec))
        self.text.insert(2.0, '\nОшибок на одну машинную команду, оставшихся в система: ' + str(self.er))
        self.text.insert(3.0, '\nВероятность безотказной работы на интервале от 0 до t: ' + str(self.tcp) + '%')
        self.text.insert(4.0, '\nИнтенсивность отказов программы λ: ' + str(self.lambdaa) + '\n')


    def clear(self):
        self.text.delete('1.0', tk.END)