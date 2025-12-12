#!/bin/python3

import sys
import os
import ctypes
import platform
import pyperclip as pc
from PyQt6.QtWidgets import (QApplication, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
                            QHBoxLayout, QFrame, QPushButton, QHeaderView, QLabel)
from PyQt6.QtGui import QColor, QBrush, QIcon
from PyQt6.QtCore import QTimer, Qt, QPoint, QObject, pyqtSignal
from pynput import keyboard
import math

a, text = "", ""
z, x, a = 0, 0, 0
z1, x1, a1 = 0, 0, 0
z2, x2, a2 = 0, 0, 0
z3, x3, a3 = 0, 0, 0
dn, do = 0, 0
drag_pos = None
pf = platform.system()

base = [["X-Coord", "Z-Coord", "Angle", "Distance"],
        ["~", "~", "~", ""],
        ["~", "~", "~", ""],
        ["Nether :", "", "", ""],
        ["~", "~", "~", "~"],
        ["Overworld :", "", "", ""],
        ["~", "~", "~", "~"]]

d = pc.paste().strip().split()

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class Comm(QObject):
    toggle = pyqtSignal()
    resetSig = pyqtSignal()

comm = Comm()

def titlebar():
  bar.setFixedSize(400, 30)
  bar.setStyleSheet("background-color: #222222")
  bar_layout.setContentsMargins(0, 0, 10, 0)
  bar_layout.setSpacing(10)

  bar_layout.addStretch()

  title = QLabel("EyeCalc", bar)
  title.setGeometry(0, 0, 400, 30)
  title.setAlignment(Qt.AlignmentFlag.AlignCenter)
  title.setStyleSheet("color: white; font-weight: bold; border: none;")
  bar_layout.addStretch()

  butsize = 20

  if(pf == "Windows"):
    pad_dash = "padding-bottom: 2px;"
    pad_cross = "padding-bottom: 4px;"
  else:
    pad_dash, pad_cross = "", ""

  minbut = QPushButton("─")
  minbut.clicked.connect(minbut_clicked)
  minbut.setFixedSize(butsize, butsize)
  minbut.setStyleSheet(f"""
    QPushButton {{background-color: transparent; color: white; border: none; border-radius: 10px; {pad_dash}}}
    QPushButton:hover {{background-color: #444; border-radius: 10px;}}
    QPushButton:pressed {{background-color: #919191; border-radius: 10px;}}""")
  bar_layout.addWidget(minbut)

  closebut = QPushButton("🗙")
  closebut.clicked.connect(closebut_clicked)
  closebut.setFixedSize(butsize, butsize)
  closebut.setStyleSheet(f"""
    QPushButton {{background-color: #bf433f; color: black; border: none; border-radius: 10px; {pad_cross}}}
    QPushButton:hover {{background-color: #ff1100; border-radius: 10px;}}
    QPushButton:pressed {{background-color: #9d00ff; border-radius: 10px;}}""")
  bar_layout.addWidget(closebut)

  bar.mousePressEvent = mousePressEvent
  bar.mouseMoveEvent = mouseMoveEvent
  bar.mouseReleaseEvent = mouseReleaseEvent

  layout.addWidget(bar)

def closebut_clicked():
  window.close()

def minbut_clicked():
  hidewindow()

def mousePressEvent(event):
  global drag_pos
  if event.button() == Qt.MouseButton.LeftButton:
    drag_pos = event.globalPosition().toPoint() - window.pos()
    event.accept()

def mouseMoveEvent(event):
  global drag_pos
  if event.buttons() == Qt.MouseButton.LeftButton and drag_pos:
    window.move(event.globalPosition().toPoint() - drag_pos)
    event.accept()

def mouseReleaseEvent(event):
  global drag_pos
  drag_pos = None
  event.accept()

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
        item.setForeground(QBrush(QColor("gray")))
        table.setItem(j, i, item)

def showwindow():
  if(pf == "Windows"):
    pass
  else:
    window.setWindowState(Qt.WindowState.WindowNoState)
  window.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)
  window.setAttribute(Qt.WidgetAttribute.WA_ShowWithoutActivating, True)
  QTimer.singleShot(10, lambda: window.show())

def hidewindow():
  window.showMinimized()

def togglevis():
  if(window.isMinimized() or not window.isVisible()):
    showwindow()
  else:
    hidewindow()

comm.toggle.connect(togglevis)
comm.resetSig.connect(reset)

hotkeys = keyboard.GlobalHotKeys(
  {"<ctrl>+[": comm.resetSig.emit,
   "<ctrl>+]": comm.toggle.emit})

hotkeys.start()

def setup():
  if(d.count("/execute") == 1 and len(d) == 11 and (c for c in d[6:] if type(float(c)) == '<class \'float\'>')):
    pc.copy("")

  table.setRowCount(7)
  table.setColumnCount(4)

  layout.addWidget(table)
  layout.setContentsMargins(0, 0, 0, 0)
  layout.setSpacing(0)
  window.setLayout(layout)

  table.verticalHeader().setVisible(False)
  table.horizontalHeader().setVisible(False)
  table.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
  table.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
  table.setFocusPolicy(Qt.FocusPolicy.NoFocus)
  table.setSelectionMode(QTableWidget.SelectionMode.NoSelection)
  table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
  table.setShowGrid(False)
    
  table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
  table.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

  button.setFixedSize(100, 30)
  button.setStyleSheet("""QPushButton {background-color: #1c1c1c; color: white; border: none; padding: 5px;}
                          QPushButton:hover {background-color: #080808;}
                          QPushButton:pressed {background-color: red;}""")
  button.clicked.connect(reset)
  button_layout.addWidget(button)
  layout.addWidget(but_cont)

  for i in range(0, 4):
    for j in range(0, 7):
      t = base[j][i]

      item = QTableWidgetItem(t)
      item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
      item.setFlags(Qt.ItemFlag.ItemIsEnabled)

      if(j == 0):
        item.setForeground(QBrush(QColor("#ffffff")))
        item.setBackground(QBrush(QColor("#191919")))
      elif(j == 3):
        item.setForeground(QBrush(QColor("lime")))
        item.setBackground(QBrush(QColor("#191919")))
      elif(j == 5):
        item.setForeground(QBrush(QColor("yellow")))
        item.setBackground(QBrush(QColor("#191919")))
      else:
        item.setForeground(QBrush(QColor("gray")))

      table.setItem(j, i, item)

  timer = QTimer(window)
  timer.timeout.connect(checkClip)
  timer.start(50)

def checkClip():
  global a, text, z, x, a, z1, x1, a1, z2, x2, a2, z3, x3, a3, dn, do
  a = text
  text = pc.paste().strip()
  if(text != a):
    b = text.split()
    if(b.count("/execute") == 1 and len(b) == 11 and (c for c in b[6:] if type(float(c)) == '<class \'float\'>')):
      if(window.isMinimized() or not window.isVisible()):
        showwindow()
      else:
        pass
      x, z, a = float(b[6]), float(b[8]), float(b[9])
      if(z1 == 0 and x1 == 0 and a1 == 0):
        x1, z1, a1 = x, z, a
        lst = [x1, z1, a1, ""]
        for i in range(0, 4):
          for j in range(1, 7):
            if(j == 1):
              item = QTableWidgetItem(str(lst[i]))
              item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
              item.setForeground(QBrush(QColor("white")))
              table.setItem(1, i, item)
            elif(j == 3 or j == 5):
              continue
            else:
              t = base[j][i]
              item = QTableWidgetItem(t)
              item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
              item.setForeground(QBrush(QColor("gray")))
              table.setItem(j, i, item)

      if(z != z1 and x != x1 and a != a1):
        x2, z2, a2 = x, z, a
        lst = [x2, z2, a2, ""]
        for i in range(0, 4):
          item = QTableWidgetItem(str(lst[i]))
          item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
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
          item.setForeground(QBrush(QColor("lime")))
          table.setItem(4, i, item)

        lst = [round(x3), round(z3), a1, round(do)]
        for i in range(0, 4):
          item = QTableWidgetItem(str(lst[i]))
          item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
          item.setForeground(QBrush(QColor("yellow")))
          table.setItem(6, i, item)

        z1, x1, a1 = 0, 0, 0
        z2, x2, a2 = 0, 0, 0
        z3, x3, a3 = 0, 0, 0
        pc.copy("")
        text = ""

app = QApplication(sys.argv)

if(os.name == "nt"):
  appid = "eyecalc.calc.1.0"
  try:
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(appid)
  except Exception:
    pass

if(os.name == "posix"):
  app.setDesktopFileName("EyeCalc")

window = QWidget()
window.setWindowTitle("EyeCalc")

icon_path = resource_path("app.ico")
app_icon = QIcon(icon_path)
window.setWindowIcon(app_icon)
app.setWindowIcon(app_icon)

scwidth = window.screen().size().width()
scheight = window.screen().size().height()

window.setGeometry(scwidth - 400, 40, 400, 235)
window.setFixedSize(400, 235)
window.setStyleSheet("background-color: #272727")
window.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint | Qt.WindowType.FramelessWindowHint)
window.setAttribute(Qt.WidgetAttribute.WA_ShowWithoutActivating, True)
window.show()

layout = QVBoxLayout(window)

bar = QWidget()
bar_layout = QHBoxLayout(bar)

but_cont = QWidget()
button_layout = QHBoxLayout(but_cont)
button_layout.setContentsMargins(0, 0, 0, 0)
button_layout.addStretch()
button = QPushButton("Reset")

table = QTableWidget()

titlebar()

setup()

sys.exit(app.exec())
