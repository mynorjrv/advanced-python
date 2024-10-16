import random
from tkinter import Tk
from tkinter import StringVar, IntVar
from tkinter import N, W, E, S
from tkinter import ttk
from tkinter import messagebox

def running(*args):
    # button.config()
    # print(mainframe.cget("width"))
    x_now = x.get()
    y_now = y.get()
    dist_x = random.randint(int(398/4), int(3*398/4))
    dist_y = random.randint(int(458/4), int(3*458/4))
    desp_x = int((x_now+100+dist_x)%398)
    desp_y = int((y_now+40+dist_y)%458)
    x.set(desp_x)
    y.set(desp_y)
    button.place(x=x.get(), y=y.get(), width=100, height=40)
    # button.config(text="You got me :(")

    # keys = mainframe.keys()
    # for key in keys:
    #     print(f'Atribute: {key}', end=' ')
    #     value = mainframe[key]
    #     vtype = type(value)
    #     print(f'Type: {vtype} Value: {value:}')
# window.bind("<Button-1>", my_callback)

def not_running(*args):
    # button.config()
    # print(button.cget("width"))
    button.config(text="Catch me :)")
# window.bind("<Button-1>", my_callback)

root = Tk()
# root.geometry("500x500")
root.minsize(width=500, height=500)
root.maxsize(width=500, height=500)
# root.resizable()
root.title("Catch me if you can!")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

mainframe = ttk.Frame(
    root, width=498, height=498, padding="1 1 1 1"
)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

button = ttk.Button(
    mainframe, text="Catch me :)"
)
x = IntVar(mainframe, 0)
y = IntVar(mainframe, 0)
button.place(x=x.get(), y=y.get(), width=100, height=40)
button.bind('<Enter>', running)
button.bind('<Leave>', not_running)

root.mainloop()