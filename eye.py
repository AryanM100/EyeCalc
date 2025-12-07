#!/bin/python3

import sys
import pyperclip as pc
from PyQt6.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, QHBoxLayout, QFrame, QPushButton, QHeaderView
from PyQt6.QtGui import QColor, QBrush
from PyQt6.QtCore import QTimer, Qt
from pynput import keyboard
import math

a, text = "", ""
z, x, a = 0, 0, 0
z1, x1, a1 = 0, 0, 0
z2, x2, a2 = 0, 0, 0
z3, x3, a3 = 0, 0, 0
dn, do = 0, 0

base = [["X-Coord", "Z-Coord", "Angle", "Distance"],
        ["~", "~", "~", ""],
        ["~", "~", "~", ""],
        ["Nether :", "", "", ""],
        ["~", "~", "~", "~"],
        ["Overworld :", "", "", ""],
        ["~", "~", "~", "~"]]

d = pc.paste().strip().split()

def setup():
  if(d.count("/execute") == 1 and len(d) == 11 and (c for c in d[6:] if type(float(c)) == '<class \'float\'>')):
    pc.copy("")

  table.setRowCount(7)
  table.setColumnCount(4)

  layout.addWidget(table)
  # layout.addWidget(button)
  # layout.addStretch()
  layout.setContentsMargins(0, 0, 0, 0)
  layout.setSpacing(0)
  window.setLayout(layout)

  table.verticalHeader().setVisible(False)
  table.horizontalHeader().setVisible(False)
  table.verticalScrollBar().hide()
  table.horizontalScrollBar().hide()
  table.setShowGrid(False)

  table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
  table.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

  button.setFixedSize(100, 30)
  button.setStyleSheet("""
            QPushButton {
                background-color: #1c1c1c;
                color: white;
                border: none;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #080808;
            }
            QPushButton:pressed {
                background-color: red;
            }
        """)
  button.clicked.connect(reset)
  button_layout.addWidget(button)
  layout.addWidget(but_cont)

  for i in range(0, 4):
    for j in range(0, 7):
      t = base[j][i]

      item = QTableWidgetItem(t)
      item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
      item.setFlags(Qt.ItemFlag.ItemIsEditable)

      if(j == 0):
        item.setForeground(QBrush(QColor("red")))
        item.setBackground(QBrush(QColor("#191919")))
      elif(j == 3):
        item.setForeground(QBrush(QColor("lime")))
        item.setBackground(QBrush(QColor("#191919")))
      elif(j == 5):
        item.setForeground(QBrush(QColor("yellow")))
        item.setBackground(QBrush(QColor("#191919")))

      table.setItem(j, i, item)

  timer = QTimer(window)
  timer.timeout.connect(checkClip)
  timer.start(50)

def reset():
  global a, text, z, x, a, z1, x1, a1, z2, x2, a2, z3, x3, a3, dn, do

  z1, x1, a1 = 0, 0, 0
  z2, x2, a2 = 0, 0, 0
  z3, x3, a3 = 0, 0, 0
  pc.copy("")
  text = ""
  for i in range(0,4):
    for j in range(1, 7):
      if(j == 3 or j == 5):
        continue
      else:
        t = base[j][i]
        item = QTableWidgetItem(t)
        item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        item.setFlags(Qt.ItemFlag.ItemIsEditable)
        table.setItem(j, i, item)

def checkClip():
  global a, text, z, x, a, z1, x1, a1, z2, x2, a2, z3, x3, a3, dn, do
  a = text
  text = pc.paste().strip()

  if(text != a):
    b = text.split()
    if(b.count("/execute") == 1 and len(b) == 11 and (c for c in b[6:] if type(float(c)) == '<class \'float\'>')):
      x, z, a = float(b[6]), float(b[8]), float(b[9])
      if(z1 == 0 and x1 == 0 and a1 == 0):
        x1, z1, a1 = x, z, a
        lst = [x1, z1, a1, ""]
        for i in range(0, 4):
          for j in range(1, 7):
            if(j == 1):
              item = QTableWidgetItem(str(lst[i]))
              item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
              item.setFlags(Qt.ItemFlag.ItemIsEditable)
              item.setForeground(QBrush(QColor("white")))
              table.setItem(1, i, item)
            elif(j == 3 or j == 5):
              continue
            else:
              t = base[j][i]
              item = QTableWidgetItem(t)
              item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
              item.setFlags(Qt.ItemFlag.ItemIsEditable)
              table.setItem(j, i, item)

      if(z != z1 and x != x1 and a != a1):
        x2, z2, a2 = x, z, a
        lst = [x2, z2, a2, ""]
        for i in range(0, 4):
          item = QTableWidgetItem(str(lst[i]))
          item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
          item.setFlags(Qt.ItemFlag.ItemIsEditable)
          item.setForeground(QBrush(QColor("white")))
          table.setItem(2, i, item)

        m1 = math.tan(-a1 * math.pi / 180)
        m2 = math.tan(-a2 * math.pi / 180)

        z3 = (m2 * z2 - m1 * z1 + x1 - x2) / (m2 - m1)
        x3 = m1 * (z3 - z1) + x1

        do = math.sqrt((x3 - x1)**2 + (z3 - z1)**2)
        dn = do / 8

        lst = [round(x3/8), round(z3/8), a1, round(dn)]
        for i in range(0, 4):
          item = QTableWidgetItem(str(lst[i]))
          item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
          item.setFlags(Qt.ItemFlag.ItemIsEditable)
          item.setForeground(QBrush(QColor("lime")))
          table.setItem(4, i, item)

        lst = [round(x3), round(z3), a1, round(do)]
        for i in range(0, 4):
          item = QTableWidgetItem(str(lst[i]))
          item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
          item.setFlags(Qt.ItemFlag.ItemIsEditable)
          item.setForeground(QBrush(QColor("yellow")))
          table.setItem(6, i, item)

        z1, x1, a1 = 0, 0, 0
        z2, x2, a2 = 0, 0, 0
        z3, x3, a3 = 0, 0, 0
        pc.copy("")
        text = ""

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("EyeCalc")

scwidth = window.screen().size().width()
scheight = window.screen().size().height()

window.setGeometry(scwidth, 40, 400, 190)
window.setFixedSize(400, 190)
window.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint, True)
window.setAttribute(Qt.WidgetAttribute.WA_ShowWithoutActivating)
window.show()

layout = QVBoxLayout(window)

but_cont = QWidget()
button_layout = QHBoxLayout(but_cont)
button_layout.setContentsMargins(0, 0, 0, 0)
button_layout.addStretch()
button = QPushButton("Reset")

table = QTableWidget()

setup()

# checkClip()

sys.exit(app.exec())
