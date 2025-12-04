#!/bin/python3

import pyperclip as pc
import tkinter as tk
from tkinter import ttk
import math

a, text = "", ""
z, x, a = 0, 0, 0
z1, x1, a1 = 0, 0, 0
z2, x2, a2 = 0, 0, 0
z3, x3, a3 = 0, 0, 0
dn, do = 0, 0
head = ["X-Coord", "Z-Coord", "Angle", "Distance"]
d = pc.paste().strip().split()

if(d.count("/execute") == 1 and len(d) == 11 and (c for c in d[6:] if type(float(c)) == '<class \'float\'>')):
  pc.copy('')

def checkClip():
  global a, text, z, x, a, z1, x1, a1, z2, x2, a2, z3, x2, a3, dn, do
  a = text
  text = pc.paste().strip()

  if(text != a):
    b = text.split()
    if(b.count("/execute") == 1 and len(b) == 11 and (c for c in b[6:] if type(float(c)) == '<class \'float\'>')):
      x, z, a = float(b[6]), float(b[8]), float(b[9])
      if(z1 == 0 and x1 == 0 and a1 == 0):
        x1, z1, a1 = x, z, a
        lst = [x1, z1, a1, "~"]
        for i in range(0,4):
          for j in range(1, 7):
            if(j == 1):
              c2 = tk.Label(root, width=15, bg="#3F3F3F", text=lst[i], anchor="center", fg="white")
              c2.grid(row=1, column=i)
            elif(j == 3 or j == 5):
              continue
            else:
              c1 = tk.Label(root, width=15, bg="#3F3F3F", text="~", anchor="center", fg="white")
              c1.grid(row=j, column=i)

      if(z != z1 and x != x1 and a != a1):
        x2, z2, a2 = x, z, a

        lst = [x2, z2, a2]
        for i in range(0,3):
          c3 = tk.Label(root, width=15, bg="#3F3F3F", text=lst[i], anchor="center", fg="white")
          c3.grid(row=2, column=i)

        m1 = math.tan(-a1 * math.pi / 180)
        m2 = math.tan(-a2 * math.pi / 180)

        z3 = (m2 * z2 - m1 * z1 + x1 - x2) / (m2 - m1)
        x3 = m1 * (z3 - z1) + x1

        do = math.sqrt((x3 - x1)**2 + (z3 - z1)**2)
        dn = do / 8

        lst = [round(x3/8), round(z3/8), a1, round(dn)]
        for i in range(0,4):
          c4 = tk.Label(root, width=15, bg="#3F3F3F", text=lst[i], anchor="center", fg="lime")
          c4.grid(row=4, column=i)

        lst = [round(x3), round(z3), a1, round(do)]
        for i in range(0,4):
          c5 = tk.Label(root, width=15, bg="#3F3F3F", text=lst[i], anchor="center", fg="yellow")
          c5.grid(row=6, column=i)
        
        z1, x1, a1 = 0, 0, 0
        z2, x2, a2 = 0, 0, 0
        z3, x3, a3 = 0, 0, 0

  root.after(50, checkClip)

root = tk.Tk()
root.title("EyeCalc")

scwidth = root.winfo_screenwidth()
scheight = root.winfo_screenheight()

root.geometry(f"490x200+{scwidth}+0")
s = ttk.Style()
s.configure('My.TFrame', background="#262626")
frm = ttk.Frame(root, style="My.TFrame")
frm.place(height=250, width=500, x=0, y=0)
frm.config()
root.resizable(False, False)

for i in range(0,4):
  for j in range(0, 7):
    if(j == 0):
      c1 = tk.Label(root, width=15, bg="#3F3F3F", text=head[i], anchor="center", fg="#fc7474")
      c1.grid(row=j, column=i)
    elif(j == 3):
      c1 = tk.Label(root, width=15, bg="#3F3F3F", text="Nether :", anchor="center", fg="lime").grid(row=3, column=0)
    elif(j == 5):
      c1 = tk.Label(root, width=15, bg="#3F3F3F", text="Overworld :", anchor="center", fg="yellow").grid(row=5, column=0)
    else:
      c1 = tk.Label(root, width=15, bg="#3F3F3F", text="~", anchor="center", fg="white")
      c1.grid(row=j, column=i)

checkClip()

root.mainloop()