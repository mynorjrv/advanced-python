import tkinter as tk

window = tk.Tk()

canvas = tk.Canvas(window, width=400, height=400, bg='black')
canvas.create_rectangle(200, 100, 300, 300, outline='white', width=5, fill='red')

canvas2 = tk.Canvas(window, width=400, height=400, bg='black')
canvas2.create_polygon(20, 380, 200, 68, 380, 380, outline='red', width=5, fill='yellow')

canvas3 = tk.Canvas(window, width=400, height=400, bg='blue')
canvas3.create_oval(100, 100, 300, 200, outline='red', width=20, fill='white')

canvas4 = tk.Canvas(window, width=400, height=400, bg='yellow')
canvas4.create_arc(10, 100, 380, 300, outline='red', width=5)
canvas4.create_arc(10, 100, 380, 300, outline='blue', width=5,
                  style=tk.CHORD, start=90, fill='white')
canvas4.create_arc(10, 100, 380, 300, outline='green', width=5,
                  style=tk.ARC, start=180, extent=180)

canvas5 = tk.Canvas(window, width=400, height=400, bg='blue')
canvas5.create_text(200, 200, text="Mary\nhad\na\nlittle\nlamb",
                   font=("Arial","40","bold"),
                   justify=tk.CENTER,
                   fill='white')

canvas6 = tk.Canvas(window, width=400, height=400, bg='yellow')
canvas6.create_arc(10, 100, 380, 300, outline='red', width=5,
                   start=15)
canvas6.create_arc(10, 100, 380, 300, outline='blue', width=5,
                  style=tk.CHORD, start=90+15, fill='white')
canvas6.create_arc(10, 100, 380, 300, outline='green', width=5,
                  style=tk.ARC, start=180+15, extent=180)

image = tk.PhotoImage(file='./Python-advanced-3-GUI/image.png')
canvas7 = tk.Canvas(window, width=400, height=400, bg='yellow')
canvas7.create_image(200, 200, image=image)

# import PIL
# canvas = tk.Canvas(window, width=400, height=400, bg='red')
# jpg = PIL.Image.open('logo.jpg')
# image = PIL.ImageTk.PhotoImage(jpg)
# canvas.create_image(200, 200, image=image)

button = tk.Button(window, text="Quit", command=window.destroy)

canvas.grid(row=0, column=0)
canvas2.grid(row=1, column=0)
canvas3.grid(row=0, column=1)
canvas4.grid(row=1, column=1)
canvas5.grid(row=0, column=2)
canvas6.grid(row=1, column=2)
canvas7.grid(row=0, column=3)
button.grid(row=2, columnspan=4)

window.mainloop()
