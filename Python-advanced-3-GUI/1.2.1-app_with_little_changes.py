import tkinter
from tkinter import messagebox


def Click():
    replay = messagebox.askquestion("Quit?", "Are you sure?")
    if replay == 'yes':
        skylight.destroy()


skylight = tkinter.Tk()
skylight.title("Skylight")
button = tkinter.Button(skylight, text="Bye!", command=Click)
button.place(x=10, y=10)
button = tkinter.Button(skylight, text="Another bye!", command=Click)
button.place(x=10, y=40)
skylight.mainloop()
