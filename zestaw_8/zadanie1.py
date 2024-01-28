import tkinter as tk
from tkinter import StringVar, Button, Entry
import tkinter.font as font

okno = tk.Tk()
okno.title("Calculator")

myFont = font.Font(family="Arial", size=20, weight="bold")

ans_entry = Entry(okno, bd=5, width=20, font=myFont, bg="gray", fg="white")
ans_entry.grid(row=0, column=0, columnspan=4)


# Buttons
btn = list()
symbols = ["+", "=", "0", "C", "-", "*", "/"]

r = 1
col = 0

for i in range(1, 10):
    btn.append(Button(okno, text=str(i), padx=20, pady=10))
    btn[-1]["font"] = myFont
    btn[-1].grid(row=r, column=col)

    col += 1

    if i % 3 == 0:
        btn.append(Button(okno, text=symbols.pop(), padx=20, pady=10))
        btn[-1]["font"] = myFont
        btn[-1].grid(row=r, column=col)
        r += 1
        col = 0


while len(symbols) > 0:
    btn.append(Button(okno, text=symbols.pop(), padx=20, pady=10))
    btn[-1]["font"] = myFont
    btn[-1].grid(row=r, column=col)
    col += 1


# proponuje dopisywac do slownika trzy elementy:
# num_1, num_2, oper wraz z wartościami
equation = {}


def mouse_button_release(event):
    widg = event.widget
    text = widg.cget("text")

    if text in "0123456789":
        ans_entry.insert(len(ans_entry.get()), text)

    if text in "+-*/":
        equation["oper"] = text
        if ans_entry.get() and ans_entry.get()[-1] in "+-*/":
            ans_entry.delete(len(ans_entry.get()) - 1, "end")
        ans_entry.insert("end", equation["oper"])

    if text == "C":
        ans_entry.delete(0, "end")

    if text == "=":
        operation()


def operation():
    expression = ans_entry.get()

    if "oper" in equation and equation["oper"] in "+-*/":
        try:
            result = eval(expression)
            ans_entry.delete(0, "end")
            ans_entry.insert("end", str(result))
        except:
            ans_entry.delete(0, "end")
            ans_entry.insert("end", "Error")


# sposób na reakcję
okno.bind("<ButtonRelease-1>", mouse_button_release)

okno.mainloop()
