import tkinter as tk


def click(*args):
    global size, grows
    if grows:
        size += 50
        if size >= 500:
            grows = False
    else:
        size -= 50
        if size <= 100:
            grows = True
    window.geometry(str(size) + "x" + str(size))


size = 100
grows = True
window = tk.Tk()
window.geometry("100x100")
window.bind("<Button-1>", click)
window.mainloop()
