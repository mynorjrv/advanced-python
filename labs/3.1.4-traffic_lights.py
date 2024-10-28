from tkinter import Tk
from tkinter import StringVar, IntVar
from tkinter import N, W, E, S
from tkinter import ttk
from tkinter import messagebox
from tkinter import Canvas

phases = ((True,  False, False),
          (True,  True,  False),
          (False, False, True),
          (False, True,  False),
          (True, True, True))

def change_phase(
        phases:tuple[tuple[bool, bool, bool]]
    ) -> callable:
    def inner_change_phase(
            inner_phase=phases
        ) -> None:
        phase = phase_counter.get()
        colors = inner_phase[phase]

        if colors[0]:
            canvas.itemconfig(oval_up, fill='red')
            # oval_up.config(fill='red')
        else:
            canvas.itemconfig(oval_up, fill='gray')
        
        if colors[1]:
            canvas.itemconfig(oval_middle, fill='yellow')
        else:
            canvas.itemconfig(oval_middle, fill='gray')

        if colors[2]:
            canvas.itemconfig(oval_down, fill='green')
        else:
            canvas.itemconfig(oval_down, fill='gray')

        phase_counter.set((phase+1)%(len(inner_phase)))
    return inner_change_phase

def quit():
    replay = messagebox.askquestion("Quit?", "Are you sure?")
    if replay == 'yes':
        root.destroy()

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

phase_counter = IntVar(mainframe, 0)

oval_up = canvas.create_oval(
    22.5, 22.5, 247.5, 247.5, fill='gray', outline='black'
)
oval_middle = canvas.create_oval(
    22.5, 292.5, 247.5, 517.5, fill='gray', outline='black'
)
oval_down = canvas.create_oval(
    22.5, 562.5, 247.5, 787.5, fill='gray', outline='black'
)


next_button = ttk.Button(
    mainframe, text='Next', command=change_phase(phases=phases)
)
next_button.grid(column=1, row=1)

quit_button = ttk.Button(mainframe, text='Quit', command=quit)
quit_button.grid(column=1, row=2)

root.mainloop()