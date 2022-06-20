import os
from tkinter import *
import re


files = []
file = ''


def end():
    global file, var, regex
    d = os.path.dirname(os.path.abspath(var.get()))
    os.system(f'start chrome {d}\\{var.get()}')


def radiobuttons():
    global var, row, column, regex
    for i in range(len(files)):
        f = files[i]
        text = re.sub(regex, '', f.replace('.pdf', ''), 0)
        rb = Radiobutton(master=frame, text=text, value=files[i], variable=var)
        rb.select()
        rb.grid(row=row, column=column)
        row += 1


if __name__ == '__main__':
    regex = r"\d{4}-\d{2}-\d{2}-"
    for x in os.listdir():
        if x.endswith(".pdf"):
            files.append(x)

    row = 0
    column = 0

    window = Tk()
    frame = Frame(master=window)
    label = Label(master=frame, text='Which PDF file you want to open?')
    label.grid(row=row, column=0)
    row += 1

    var = StringVar()
    radiobuttons()

    btn = Button(master=frame, text='Open', command=end)
    btn.grid(row=row, column=0)

    window.minsize(1000, 1000)
    frame.pack()
    window.mainloop()