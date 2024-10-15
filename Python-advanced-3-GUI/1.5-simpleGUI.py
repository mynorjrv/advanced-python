import tkinter as tk

window = tk.Tk()

label = tk.Label(window, text="Little label:")
label.pack()

frame = tk.Frame(window, height=30, width=100, bg="#000099")
frame.pack()

button = tk.Button(window, text ="Button")
button.pack(fill=tk.X)

switch = tk.IntVar()
switch.set(1)

checkbutton = tk.Checkbutton(window, text="Check Button", variable=switch)
checkbutton.pack()

entry = tk.Entry(window, width=30)
entry.pack()

# Por qué toma estos valores? O más bien, por qué es legal hacerlo?
radiobutton_1 = tk.Radiobutton(window, text="Steak", variable=switch, value=0)
radiobutton_1.pack()
radiobutton_2 = tk.Radiobutton(window, text="Salad", variable=switch, value=1)
radiobutton_2.pack()
radiobutton_3 = tk.Radiobutton(window, text="Pizza", variable=switch, value=2)
radiobutton_3.pack()
radiobutton_4 = tk.Radiobutton(window, text="Papitas", variable=switch, value=3)
radiobutton_4.pack()

window.mainloop()
