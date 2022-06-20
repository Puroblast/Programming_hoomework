from tkinter import *
from tkinter import messagebox
import gspread
import datetime
import pandas as pd
import matplotlib.pyplot as plt

def alert(title, message, type_of_alert='info'):
    show_method = getattr(messagebox, 'show{}'.format(type_of_alert))
    show_method(title, message)


def finish(event):
    global sin_mass, sin_radius, filename
    mass = str(int(sin_mass.get()))
    radius = str(int(sin_radius.get()))
    gsheet.update('B1', str(datetime.date.today()))
    gsheet.update('B3', mass)
    gsheet.update('B4', radius)
    name = str(datetime.date.today()) + '-' + filename.get()
    fig, ax = plt.subplots()
    ax.axis('off')
    df = pd.DataFrame(gsheet.get_all_records())
    ax.table(cellText=df.values, colLabels=df.columns, loc='center')
    plt.savefig(f'{name}.pdf')
    alert('Success!', 'Data successfully saved!')



gc = gspread.service_account(filename="Token.json")
gsheet = gc.open("MySheet").worksheet("3")

window = Tk()
frame = Frame(master=window)
label_mass = Label(master=frame, text='Mass:')
label_mass.grid(row=0, column=0)
sin_mass = Entry(master=frame)
sin_mass.grid(row=0, column=1)
label_radius = Label(master=frame, text='Radius:')
label_radius.grid(row=1, column=0)
sin_radius = Entry(master=frame)
sin_radius.grid(row=1, column=1)

label_name = Label(master=frame, text='Name of PDF file:')
label_name.grid(row=3, column=0)
filename = Entry(master=frame)
filename.grid(row=3, column=1)
btn_confirm = Button(master=frame, text='Confirm')
btn_confirm.grid(row=4, column=0)
btn_confirm.bind('<Button-1>', finish)

frame.pack()
window.mainloop()