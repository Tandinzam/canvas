'''import tkinter as tk
root =tk.Tk()
root.title("My first canvas")
canvas=tk.Canvas(root, width=500,
                  height=350, bg="white")
canvas.pack()
canvas.create_rectangle(40, 40, 220, 150, fill="coral")
canvas.create_oval(280, 50, 440, 190, fill="light blue")
canvas.create_line(50, 250, 500, 250, width=4)
canvas.create_text(275, 310, text="Hello Canvas", font=("Arial, 20"))
root.mainloop()'''


import tkinter as tk

root = tk.Tk()
root.title("My Simple House")

canvas = tk.Canvas(root, width=600, height=400, bg="skyblue")
canvas.pack()

# House body
canvas.create_rectangle(180, 180, 420, 350, fill="lightyellow")

# Roof
canvas.create_polygon(150, 180, 300, 70, 450, 180, fill="brown")

# Door
canvas.create_rectangle(270, 260, 330, 350, fill="saddlebrown")

# Left window
canvas.create_rectangle(210, 210, 260, 260, fill="lightblue")

# Right window
canvas.create_rectangle(340, 210, 390, 260, fill="lightblue")

# Door knob
canvas.create_oval(315, 305, 322, 312, fill="black")

# Sun
canvas.create_oval(470, 40, 530, 100, fill="yellow")

# Ground
canvas.create_line(0, 350, 600, 350, width=3)

root.mainloop()