import random
from tkinter import Tk
from tkinter import StringVar, IntVar, BooleanVar
from tkinter import N, W, E, S
from tkinter import ttk
from tkinter import messagebox


def count_time():
    if counting_state.get():
        counter.set(counter.get()+1)
        label.config(text=f"Counted seconds: {counter.get()}")
        label.after(1000, count_time)

def start_counting():
    if not counting_state.get():
        counting_state.set(True)
        label.after(1000, count_time)
        # count_time()

def stop_counting():
    if counting_state.get():
        counting_state.set(False)


root = Tk()
root.title("Counting")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

mainframe = ttk.Frame(root, padding="1 1 1 1")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure([0, 1], weight=1)
mainframe.rowconfigure([0, 1], weight=1)

counting_state = BooleanVar(mainframe, False)

start_button = ttk.Button(
    mainframe, text="Start", command=start_counting
)
start_button.grid(column=0, row=0, sticky=(N, W, E, S))

end_button = ttk.Button(
    mainframe, text="End", command=stop_counting
)
end_button.grid(column=1, row=0, sticky=(N, W, E, S))

counter = IntVar(mainframe, 0)

label = ttk.Label(
    master=mainframe, 
    text=f"Counted seconds: 0"
)
label.grid(column=0, row=1, columnspan=2)


# is_white = True
# window = tk.Tk()
# frame = tk.Frame(window, width=200, height=100, bg='white')
# frame.after(100, blink)
# frame.pack()
root.mainloop()
