
import tkinter as tk

def click1():
    entry.insert(tk.END, "1")

def click2():
    entry.insert(tk.END, "2")

def click3():
    entry.insert(tk.END, "3")

def click4():
    entry.insert(tk.END, "4")

def click5():
    entry.insert(tk.END, "5")

def click6():
    entry.insert(tk.END, "6")

def click7():
    entry.insert(tk.END, "7")

def click8():
    entry.insert(tk.END, "8")

def click9():
    entry.insert(tk.END, "9")

def click0():
    entry.insert(tk.END, "0")

def clickA():
    entry.insert(tk.END, "+")

def clickB():
    entry.insert(tk.END, "-")

def clickC():
    entry.insert(tk.END, "*")

def clickD():
    entry.insert(tk.END, "/")


def calculate():
    expression = entry.get()

    if not expression:
        return

    if not all(c in "0123456789+-*/" for c in expression):
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Ошибка")
        return

    try:
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))

    except ZeroDivisionError:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Деление на ноль!")

    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Ошибка")

root = tk.Tk()
root.configure(bg="#222831")

entry = tk.Entry(root)
entry.place(x=160, y=100)

button = tk.Button(root, text='1', command=click1, width=10, height=4, bg="#00ADB5", fg="white")
button.place(x=100, y=290)

button2 = tk.Button(root, text='2', command=click2, width=10, height=4, bg="#00ADB5", fg="white")
button2.place(x=180, y=290)

button3 = tk.Button(root, text='3', command=click3, width=10, height=4, bg="#00ADB5", fg="white")
button3.place(x=260, y=290)

button4 = tk.Button(root, text='4', command=click4, width=10, height=4, bg="#00ADB5", fg="white")
button4.place(x=100, y=220)

button5 = tk.Button(root, text='5', command=click5, width=10, height=4, bg="#00ADB5", fg="white")
button5.place(x=180, y=220)

button6 = tk.Button(root, text='6', command=click6, width=10, height=4, bg="#00ADB5", fg="white")
button6.place(x=260, y=220)

button7 = tk.Button(root, text='7', command=click7, width=10, height=4, bg="#00ADB5", fg="white")
button7.place(x=100, y=150)

button8 = tk.Button(root, text='8', command=click8, width=10, height=4, bg="#00ADB5", fg="white")
button8.place(x=180, y=150)

button9 = tk.Button(root, text='9', command=click9, width=10, height=4, bg="#00ADB5", fg="white")
button9.place(x=260, y=150)

button0 = tk.Button(root, text='0', command=click0, width=10, height=4, bg="#00ADB5", fg="white")
button0.place(x=180, y=361.2)

buttonA = tk.Button(root, text='+', command=clickA, width=10, height=4, bg="#006C72", fg="white")
buttonA.place(x=380, y=150)

buttonB = tk.Button(root, text='-', command=clickB, width=10, height=4, bg="#006C72", fg="white")
buttonB.place(x=380, y=221)

buttonC = tk.Button(root, text='*', command=clickC, width=10, height=4, bg="#006C72", fg="white")
buttonC.place(x=380, y=292)

buttonD = tk.Button(root, text='/', command=clickD, width=10, height=4, bg="#006C72", fg="white")
buttonD.place(x=380, y=363)

buttonE = tk.Button(root, text='=', command=calculate, width=10, height=4, bg="#66CDD3", fg="white")
buttonE.place(x=260, y=360)

root.geometry("500x480")
root.resizable(False, False)
root.mainloop()