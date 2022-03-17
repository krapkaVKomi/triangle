from tkinter import Message
from attr import attributes
import math
from tkinter import *
import tkinter as tk
from tkinter import messagebox


class Triangle():   
    ''' Атрибути довільного трикутника '''
    def __init__(self, side1, side2, side3):  
        # cторони
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        # периметр
        self.perimeter = side1 + side2 + side3
        # площа
        a = float(self.side1)
        b = float(self.side2)
        c = float(self.side3)
        p = (a + b + c)/2
        try:
            self.square = math.sqrt(p*(p-a)*(p-b)*(p-c))
        except ValueError:
            ve = 'Не коректно введені данні НЕБУВАЄ ТАКИХ ТРИКУТНИКІВ'
            messagebox.showerror("ValueError", str(ve))
            pass
        # радіус описаного кола
        try:
            self.big_r = (a*b*c) / (4*self.square) 
        except ValueError:
            ve = 'Не коректно введені данні НЕБУВАЄ ТАКИХ ТРИКУТНИКІВ'
            messagebox.showerror("ValueError", str(ve))
            pass
        # радіу вписаного кола
        try:
            self.small_r = (2*self.square) / self.perimeter
        except ValueError:
            ve = 'Не коректно введені данні НЕБУВАЄ ТАКИХ ТРИКУТНИКІВ'
            messagebox.showerror("ValueError", str(ve))
            pass


''' ФУНКЦІЇ КНОПОК '''


def info_perimeter():
    try:
        info = Triangle(float(message_entry.get()), float(message_entry2.get()), float(message_entry3.get()))
        messagebox.showinfo("Периметр", str(info.perimeter) )
    except ValueError:
        ve = 'Не коректно введені данні'
        messagebox.showerror("ValueError", str(ve))

def info_square():
    try:
        info = Triangle(float(message_entry.get()), float(message_entry2.get()), float(message_entry3.get()))
        messagebox.showinfo("Площа", str(info.square) )
    except ValueError:
        ve = 'Не коректно введені данні'
        messagebox.showerror("ValueError", str(ve))

def info_big_r():
    try:
        info = Triangle(float(message_entry.get()), float(message_entry2.get()), float(message_entry3.get()))
        messagebox.showinfo("Описане коло", str(info.big_r) )
    except ValueError:
        ve = 'Не коректно введені данні'
        messagebox.showerror("ValueError", str(ve))

def info_small_r():
    try:
        info = Triangle(float(message_entry.get()), float(message_entry2.get()), float(message_entry3.get()))
        messagebox.showinfo("Вписане коло", str(info.small_r) )
    except ValueError:
        ve = 'Не коректно введені данні'
        messagebox.showerror("ValueError", str(ve))


"""  РОЗМІТКА ВІКНА """
root = Tk()
root.title("Дослідження довільнго трикутника за сторонами")
root.geometry("450x250")
root.resizable(height = False, width = False)

label = tk.Label(text="ПЕРША сторона трикутника")
label.pack(fill=tk.X)
message_entry = Entry(root, width = 20)
message_entry.pack(fill=tk.X)

labe2 = tk.Label(text="ДРУГА сторона трикутника")
labe2.pack(fill=tk.X)
message_entry2 = Entry(root, width = 20)
message_entry2.pack(fill=tk.X)

labe3 = tk.Label(text="ТРЕТЯ сторона трикутника")
labe3.pack(fill=tk.X)
message_entry3 = Entry(root, width = 20)
message_entry3.pack(fill=tk.X)


""" КНОПКИ """

perimeter_button = Button(text="Периметр", command=info_perimeter)
perimeter_button.pack(fill=tk.X)

square_button = Button(text="Площа", command=info_square)
square_button.pack(fill=tk.X)

big_r_button = Button(text="коло описане навколо трикутника", command=info_big_r)
big_r_button.pack(fill=tk.X)

small_r_button = Button(text="коло вписане в трикутник", command=info_small_r)
small_r_button.pack(fill=tk.X)




root.mainloop()



