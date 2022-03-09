#!/usr/bin/env python

import tkinter as tk

from spinning_wheel_objs import Spinning_Wheel, WheelItem

root = tk.Tk()
width = 600
height = 600
root.geometry('{}x{}'.format(width, height))
root.title("Ethan Posner's Spinning Wheel")
root.configure(background='grey25')

pie_items = [
        WheelItem("Item 1", 1/5),
        WheelItem("Item 2", 1/5),
        WheelItem("Item 3", 1/5),
        WheelItem("Item 4", 1/5),
        WheelItem("Item 5", 1/5)
    ]


canvas_frame = tk.Frame(root)
wheel = Spinning_Wheel(canvas_frame, 200, pie_items, width=str(width), height=str(height-100))
wheel.pack(padx=0, pady=0, side="top", fill="both", expand=True)
canvas_frame.pack(side="top", padx=0, pady=5, fill="both", expand=True)

# frame for user controls
user_controls = tk.Frame(root)
user_controls.configure(background='grey25')

spin_button = tk.Button(user_controls, text="spin", command=wheel.spin)
spin_button.pack()
user_controls.pack(side='top')

wheel.draw(offset=0)

root.mainloop()
