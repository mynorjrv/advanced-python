from tkinter import Tk, StringVar, N, W, E, S
from tkinter import ttk

root = Tk()
root.title("Little app")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

fourList = [0, 1, 2, 3]
sevenList = [i for i in range(7)]

mainframe = ttk.Frame(root, padding="3 3 3 3")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(sevenList, weight=1)
mainframe.rowconfigure(sevenList, weight=1)


# mainframe['borderwidth'] = 5
# mainframe['relief'] = 'raised'

# s = ttk.Style()
# s.configure('Danger.TFrame', background='red')
# ttk.Frame(mainframe, width=200, height=200, style='Danger.TFrame').grid(
#     column=0, row=0, sticky=(N, W, E, S)
# )


# for row in fourList:
#     for column in fourList:
#         button = ttk.Button(
#             mainframe, 
#             width=20,
#             text=f'Button #{len(fourList)*row + column}'
#         )
#         button.grid(
#             column=column, row=row, 
#             sticky=(N, S, E, W)
#         )

# Rows
for row in fourList:
    for column in fourList[:-1]:
        button = ttk.Button(
            mainframe, 
            text=f'Row #{len(fourList)*row + column}'
        )
        button.grid(
            column=2*column, row=2*row,
            columnspan=3, 
            sticky=(N, S, E, W)
        )

# Columns
for row in fourList[:-1]:
    for column in fourList:
        button = ttk.Button(
            mainframe, 
            text=f'Column #{len(fourList)*row + column}'
        )
        button.grid(
            column=2*column, row=2*row,
            rowspan=3, 
            sticky=(N, S, E, W)
        )

root.mainloop()