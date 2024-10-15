from tkinter import Tk, StringVar, N, W, E, S
from tkinter import ttk

root = Tk()
root.title("Little app")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

n_by_n = 8

thicksList = [i for i in range(n_by_n)]
totalList = [i for i in range(2*len(thicksList) - 1)]

mainframe = ttk.Frame(root, padding="3 3 3 3")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure([2*i for i in thicksList], weight=0)
mainframe.columnconfigure([2*i+1 for i in thicksList[:-1]], weight=1)
mainframe.rowconfigure([2*i for i in thicksList], weight=0)
mainframe.rowconfigure([2*i+1 for i in thicksList[:-1]], weight=1)

# Five frames, 4 thicks, 1 centre
s = ttk.Style()
s.configure('f1.TFrame', background='red')
s.configure('f2.TFrame', background='blue')
s.configure('f3.TFrame', background='green')
s.configure('f4.TFrame', background='yellow')


# Rows
for row in thicksList:
    for column in thicksList[:-1]:
        rowFrame = ttk.Frame(
            mainframe, 
            width=60, height=20,
            style='f1.TFrame'
        )
        rowFrame.grid(
            column=2*column, row=2*row,
            columnspan=3, 
            sticky=(N, S, E, W)
        )

# Columns
for row in thicksList[:-1]:
    for column in thicksList:
        columnFrame = ttk.Frame(
            mainframe, 
            width=20, height=60,
            style='f2.TFrame'
        )
        columnFrame.grid(
            column=2*column, row=2*row,
            rowspan=3, 
            sticky=(N, S, E, W)
        )

# Centres
for row in thicksList[:-1]:
    for column in thicksList[:-1]:
        centreFrame = ttk.Frame(
            mainframe, 
            width=20, height=20
        )
        centreFrame.grid(
            column=(2*column + 1), row=(2*row + 1),
            sticky=(N, S, E, W)
        )


root.mainloop()