from tkinter import Tk
from tkinter import StringVar, IntVar
from tkinter import N, W, E, S
from tkinter import ttk
from tkinter import messagebox

def calculate():
    try:
        f_operand = float(first_operand.get())
        s_operand = float(second_operand.get())
    except ValueError:
        answer = messagebox.showwarning(
            'Warning', 
            "Both operands should be a number."
        )
    if operation.get()==0:
        messagebox.showinfo(
            'Sum',
            f'{f_operand}+{s_operand} = {f_operand+s_operand}'
        )
    if operation.get()==1:
        messagebox.showinfo(
            'Sub',
            f'{f_operand}-({s_operand}) = {f_operand-s_operand}'
        )
    if operation.get()==2:
        messagebox.showinfo(
            'Mul',
            f'{f_operand}*{s_operand} = {f_operand*s_operand}'
        )
    if operation.get()==3:
        if s_operand==0:
            answer = messagebox.showwarning(
                'Warning', 
                "It is not possible to divide by zero."
            )
        else:
            messagebox.showinfo(
                'Div',
                f'{f_operand}/{s_operand} = {f_operand/s_operand}'
            )

root = Tk()
root.title("Little app")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

mainframe = ttk.Frame(root, padding="3 3 3 3")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

first_operand = StringVar()
first_entry = ttk.Entry(mainframe, textvariable=first_operand)
first_entry.grid(column=0, row=0, rowspan=4)

second_operand = StringVar()
second_entry = ttk.Entry(mainframe, textvariable=second_operand)
second_entry.grid(column=2, row=0, rowspan=4)

operation = IntVar()
sum_option = ttk.Radiobutton(
    mainframe, text="+", variable=operation, value=0
)
sum_option.grid(column=1, row=0)
res_option = ttk.Radiobutton(
    mainframe, text="-", variable=operation, value=1
)
res_option.grid(column=1, row=1)
mul_option = ttk.Radiobutton(
    mainframe, text="*", variable=operation, value=2
)
mul_option.grid(column=1, row=2)
div_option = ttk.Radiobutton(
    mainframe, text="/", variable=operation, value=3
)
div_option.grid(column=1, row=3)


button = ttk.Button(
    mainframe, text=f'Calculate', command=calculate
)
button.grid(column=0, row=4, columnspan=3)


root.mainloop()