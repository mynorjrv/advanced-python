from functools import partial
import random
from tkinter import Tk
from tkinter import StringVar, IntVar
from tkinter import N, W, E, S
from tkinter import ttk
from tkinter import messagebox

# https://stackoverflow.com/questions/6920302/how-to-pass-arguments-to-a-button-command-in-tkinter
# https://tkdocs.com/shipman/extra-args.html
# https://stackoverflow.com/questions/10865116/tkinter-creating-buttons-in-for-loop-passing-command-arguments

def click(ordered_list:list[int]) -> callable:
    def inner_click(ev, inner_list=ordered_list):
        index = order_variable.get()
        print(inner_list)
        if int(button.cget('text'))==inner_list[index]:
            button.config(state='disabled')
            order_variable.set(index+1)
    return inner_click

root = Tk()
root.title("Clicker")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

mainframe = ttk.Frame(root, padding="1 1 1 1")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure([i for i in range(5)], weight=1)
mainframe.rowconfigure([i for i in range(6)], weight=1)

# Ordered list
clicker_number_list = [i+1 for i in range(25)]
clicker_number_list_copy = [i for i in range(25)]
order_variable = IntVar(mainframe, 0)

command = click(clicker_number_list_copy)

all_buttons = []
# Clicher buttons
for column in range(5):
    for row in range(5):
        this_button_number = random.choice(clicker_number_list)
        clicker_number_list.remove(this_button_number)
        button = ttk.Button(mainframe, text=f'{this_button_number}')
        button.grid(column=column, row=row, sticky=(N, W, E, S))
        button.bind('<Button-1>', command)
        all_buttons.append(button)

# Counter tag
label = ttk.Label(master=mainframe, text='Aca se va a contar')
label.grid(column=0, row=5, columnspan=5)

root.mainloop()