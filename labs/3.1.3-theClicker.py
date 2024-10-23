import copy
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


root = Tk()
root.title("Clicker")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

mainframe = ttk.Frame(root, padding="1 1 1 1")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure([i for i in range(5)], weight=1)
mainframe.rowconfigure([i for i in range(6)], weight=1)

def random_list(
        length:int=1, 
        rang:list[int, int]=None
    ) -> list[int]:
    """ Returns a list of length "len", containing non repiting
    random integers in range "rang".
    """
    if rang is None:
        rang = [1, 100]
    if len(rang)!=2:
        raise ValueError("rang needs 2 arguments")
    if rang[0]>rang[1]:
        raise ValueError("The second value should be grater")
    if rang[1]-rang[0]<length:
        raise ValueError("range in rang must be grater than length")

    random_list = []

    while len(random_list)<length:
        random_number = random.randint(rang[0], rang[1])
        if random_number in random_list:
            continue
        random_list.append(random_number)

    return random_list

# Ordered list
clicker_number_list = sorted(random_list(25, [1, 1000]))
clicker_number_list_copy = copy.copy(clicker_number_list)
order_variable = IntVar(mainframe, 0)

def click(
        ordered_list:list[int], button_number:int, button_index:int
    ) -> callable:
    def inner_click(
            ev, 
            inner_list=ordered_list, 
            inner_number=button_number, 
            inner_index=button_index
        ) -> None:
        index = order_variable.get()
        print(inner_list)
        print(inner_number)
        print(index)
        print(inner_list[index])
        if inner_number==inner_list[index]:
            all_buttons[inner_index].config(state='disabled')
            order_variable.set(index+1)
    return inner_click

all_buttons = []
# Clicher buttons
for column in range(5):
    for row in range(5):
        this_button_number = random.choice(clicker_number_list)
        clicker_number_list.remove(this_button_number)
        button = ttk.Button(mainframe, text=f'{this_button_number}')
        button.grid(column=column, row=row, sticky=(N, W, E, S))
        button.bind(
            '<Button-1>', 
            click(
                clicker_number_list_copy, 
                this_button_number,
                len(all_buttons)
            )
        )
        all_buttons.append(button)

# Counter tag
label = ttk.Label(master=mainframe, text='Aca se va a contar')
label.grid(column=0, row=5, columnspan=5)

root.mainloop()