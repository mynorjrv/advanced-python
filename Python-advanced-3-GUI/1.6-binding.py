import tkinter as tk
from tkinter import messagebox


def click():
    messagebox.showinfo("Click!","I love clicks!")

def over(ev=None):
    # messagebox.showinfo("Over!","Mouse over")
    frame.config(bg='red')

def not_over(ev=None):
    # messagebox.showinfo("Over!","Mouse over")
    frame.config(bg='#55BF40')


window = tk.Tk()
label = tk.Label(window, text="Label")
label.pack()

button = tk.Button(window, text="Button", command=click)
button.pack(fill=tk.X)

frame = tk.Frame(window, height=30, width=100, bg="#55BF40")
frame.bind('<Enter>', over)
frame.bind('<Leave>', not_over)
frame.pack()

window.mainloop()
