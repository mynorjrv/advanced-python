from tkinter import Tk
from tkinter import StringVar, IntVar
from tkinter import N, W, E, S
from tkinter import ttk
from tkinter import messagebox
from tkinter import Canvas

phases = ((True,  False, False),
          (True,  True,  False),
          (False, False, True),
          (False, True,  False))

root = Tk()
root.title("Traffic lights")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

mainframe = ttk.Frame(root, padding="1 1 1 1")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure([0, 1, 2], weight=1)
mainframe.rowconfigure([0, 1, 2], weight=1)

canvas = Canvas(mainframe, height=810, width=270, background='dark gray')
canvas.grid(column=0, row=0, columnspan=3)


oval_up = canvas.create_oval(
    22.5, 22.5, 247.5, 247.5, fill='gray', outline='black'
)
oval_middle = canvas.create_oval(
    22.5, 292.5, 247.5, 517.5, fill='gray', outline='black'
)
oval_down = canvas.create_oval(
    22.5, 562.5, 247.5, 787.5, fill='gray', outline='black'
)


next_button = ttk.Button(mainframe, text='Next')
next_button.grid(column=1, row=1)

quit_button = ttk.Button(mainframe, text='Quit')
quit_button.grid(column=1, row=2)

root.mainloop()