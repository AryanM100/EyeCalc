#!/bin/python3

import pyperclip as pc
import math

a = ""
text = ""
z, x, a = 0, 0, 0
z1, x1, a1 = 0, 0, 0
z2, x2, a2 = 0, 0, 0
z3, x3, a3 = 0, 0, 0

try:
  while(True):
    a = text
    text = pc.paste().strip()
    if(text != a):
      b = text.split()
      if(b.count("/execute") == 1 and len(b) == 11 and (c for c in b[6:] if type(float(c)) == '<class \'float\'>')):
        x, z, a = float(b[6]), float(b[8]), float(b[9])
        if(z1 == 0 and x1 == 0 and a1 == 0):
          x1, z1, a1 = x, z, a
          print(x1, z1, a1)

        if(z != z1 and x != x1 and a != a1):
          x2, z2, a2 = x, z, a
          print(x2, z2, a2)

          m1 = math.tan(-a1 * math.pi / 180)
          m2 = math.tan(-a2 * math.pi / 180)

          z3 = (m2 * z2 - m1 * z1 + x1 - x2) / (m2 - m1);
          x3 = m1 * (z3 - z1) + x1
          print(x3, z3)
          
          z1, x1, a1 = 0, 0, 0
          z2, x2, a2 = 0, 0, 0
          z3, x3, a3 = 0, 0, 0


except KeyboardInterrupt:
  print("\nExiting.")