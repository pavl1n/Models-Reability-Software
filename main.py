from tkinter import Tk, ttk
import tkinter as tk

from tab_a import Lipov as TabA
from tab_b import Shuman as TabB
from tab_c import Dzh_Moranda as TabC
from tab_d import Mills as TabD


class MainWindow(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent
        self.parent.title('Модели надёжности ПО')

        self.init_ui()

    def init_ui(self):
        self.parent['padx'] = 10
        self.parent['pady'] = 10

        self.notebook = ttk.Notebook(self, width=1000, height=700)

        a_tab = TabA(self.notebook)
        b_tab = TabB(self.notebook)
        c_tab = TabC(self.notebook)
        d_tab = TabD(self.notebook)

        self.notebook.add(a_tab, text="Модель Липова")
        self.notebook.add(b_tab, text="Модель Шумана")
        self.notebook.add(c_tab, text="Модель Джелинского-Моранды")
        self.notebook.add(d_tab, text="Модель Миллса")

        self.notebook.pack()

        self.pack()


if __name__ == '__main__':
    root = Tk()
    root.title('version')
    ex = MainWindow(root)
    root.geometry("600x650")
    root.mainloop()