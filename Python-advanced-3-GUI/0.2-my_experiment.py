from tkinter import Tk, StringVar, N, W, E, S
from tkinter import ttk

root = Tk()
root.title("Little app")

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

mainframe = ttk.Frame(root, padding="3 3 12 25")
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))



mainframe['borderwidth'] = 5
mainframe['relief'] = 'raised'

s = ttk.Style()
s.configure('Danger.TFrame', background='red', borderwidth=5, relief='raised')
ttk.Frame(mainframe, width=200, height=200, style='Danger.TFrame').grid(
    column=0, row=0, sticky=(N, W, E, S)
)

# ttk.Button(mainframe, text="Button #1").grid(column=0, row=0, sticky=(E, W))
# ttk.Button(
#     mainframe, text="Button #2"
# ).grid(
#     column=1, row=0, rowspan=2, sticky=(N, S, E, W)
# )
# ttk.Button(mainframe, text="Button #3").grid(column=0, row=1, sticky=(E, W))


root.mainloop()