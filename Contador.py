from tkinter import *
import sqlite3


class ventana:
    def __init__(self, master):
        self.master = master
        master.title("CONTADOR")

        self.lbl = Label(master, text="Numero actual del contador").pack()

        self.num = IntVar()
        self.text = Entry(master, textvariable=self.num).pack()

        self.btn = Button(master, text="Aumentar contador", command=self.boton).pack()

    def boton(self):
        ps = self.num.get()
        self.num.set(ps + 1)

root = Tk()
root.geometry("250x150+300+300")
form = ventana(root)
root.mainloop()
