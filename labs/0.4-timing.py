import datetime
import random
from tkinter import Tk
from tkinter import StringVar, IntVar, BooleanVar
from tkinter import N, W, E, S
from tkinter import ttk
from tkinter import messagebox


def count_time():
    if counting_state.get():
        counter.set(counter.get()+1)
        label.after(1000, count_time)
        # label.config(text=f"Counted seconds: {counter.get()}")
        # init_time = (
        #     datetime.datetime(1,1,1)
        #     +datetime.timedelta(milliseconds=counter.get()*1000)
        # ).strftime('%H:%M:%S.%f')[:-4]
        seconds = counter.get()
        label.config(
            text=f"Time: {int(seconds/60):02}:{seconds%60:02}"
        )

def start_counting():
    if not counting_state.get():
        label.after(1000, count_time)
        counting_state.set(True)
        # counter.set(counter.get()+1)
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

# init_time = (
#     datetime.datetime(1,1,1)+datetime.timedelta(milliseconds=0)
# ).strftime('%H:%M:%S.%f')[:-4]
label = ttk.Label(
    master=mainframe, 
    text=f"Time: 00:00"
)
label.grid(column=0, row=1, columnspan=2)


root.mainloop()
