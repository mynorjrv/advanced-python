from tkinter import Tk
from tkinter import StringVar, IntVar
from tkinter import N, W, E, S
from tkinter import ttk

root = Tk()
root.title("Clicker")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

mainframe = ttk.Frame(root, padding="1 1 1 1")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure([i for i in range(3)], weight=1)
mainframe.rowconfigure([i for i in range(1)], weight=1)


def open_this(myNum):
    print(myNum)

buttons = []
for i in range(3):
    this_button = ttk.Button(
        mainframe, text=f"Button {i}", command=lambda i=i: open_this(i)
    )
    this_button.grid(column=i, row=0)
    buttons.append(buttons)

root.mainloop()