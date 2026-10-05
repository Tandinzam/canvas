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


'''import tkinter as tk

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

import tkinter as tk

root = tk.Tk()
root.title("Dog House")

canvas = tk.Canvas(root, width=600, height=400, bg="skyblue")
canvas.pack()

# Ground
canvas.create_rectangle(0, 330, 600, 400, fill="lightgreen")

# Dog house body
canvas.create_rectangle(180, 180, 420, 330, fill="orange")

# Roof
canvas.create_polygon(
    150, 180,
    300, 70,
    450, 180,
    fill="brown"
)

# Door / entrance
canvas.create_oval(250, 210, 350, 330, fill="black")

# Small name sign
canvas.create_rectangle(260, 150, 340, 180, fill="white")
canvas.create_text(300, 165, text="DOG", font=("Arial", 12, "bold"))

# Bone
canvas.create_oval(470, 260, 490, 280, fill="white")
canvas.create_oval(510, 260, 530, 280, fill="white")
canvas.create_rectangle(480, 265, 520, 275, fill="white")

# Dog body
canvas.create_oval(60, 270, 160, 330, fill="saddlebrown")

# Dog head
canvas.create_oval(70, 220, 145, 290, fill="saddlebrown")

# Dog ears
canvas.create_oval(55, 225, 85, 270, fill="saddlebrown")
canvas.create_oval(130, 225, 160, 270, fill="saddlebrown")

# Dog eyes
canvas.create_oval(90, 240, 98, 248, fill="black")
canvas.create_oval(120, 240, 128, 248, fill="black")

# Dog nose
canvas.create_oval(105, 255, 115, 265, fill="black")

# Dog tail
canvas.create_arc(145, 275, 190, 320, start=0, extent=180, width=5)

root.mainloop()'''

import tkinter as tk

root = tk.Tk()
root.title("House with Dog House")

canvas = tk.Canvas(root, width=600, height=400, bg="skyblue")
canvas.pack()

# =========================
# GROUND
# =========================
canvas.create_rectangle(0, 350, 600, 400, fill="lightgreen")

# =========================
# MAIN HOUSE
# =========================

# House body
canvas.create_rectangle(120, 180, 370, 350, fill="lightyellow")

# Main house roof
canvas.create_polygon(
    90, 180,
    245, 70,
    400, 180,
    fill="brown"
)

# Main door
canvas.create_rectangle(215, 260, 275, 350, fill="saddlebrown")

# Door knob
canvas.create_oval(260, 300, 268, 308, fill="black")

# Left window
canvas.create_rectangle(145, 210, 195, 260, fill="lightblue")

# Right window
canvas.create_rectangle(295, 210, 345, 260, fill="lightblue")

# Window lines
canvas.create_line(170, 210, 170, 260, width=2)
canvas.create_line(145, 235, 195, 235, width=2)

canvas.create_line(320, 210, 320, 260, width=2)
canvas.create_line(295, 235, 345, 235, width=2)

# =========================
# DOG HOUSE
# =========================

# Dog house body
canvas.create_rectangle(410, 270, 550, 350, fill="orange")

# Dog house roof
canvas.create_polygon(
    395, 270,
    480, 210,
    565, 270,
    fill="darkred"
)

# Dog house entrance
canvas.create_oval(450, 295, 510, 350, fill="black")

# Dog house sign
canvas.create_text(
    480, 280,
    text="DOG",
    font=("Arial", 10, "bold")
)

# =========================
# SUN
# =========================

canvas.create_oval(480, 40, 540, 100, fill="yellow")

# =========================
# TEXT
# =========================

canvas.create_text(
    300, 380,
    text="My House and Dog House",
    font=("Arial", 16)
)

root.mainloop()