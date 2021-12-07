# !/usr/bin/python3
from tkinter import *
from tkinter import messagebox
import subprocess

top = Tk()
top.title("Franka Gripper Control")
top.geometry("300x75")

def open():
   messagebox.showinfo("Open Gripper", "Gripper Opened")

def close():
   messagebox.showinfo("Close Gripper", "Gripper Closed")

B1 = Button(top, text = "Open Gripper", command = open)
B1.place(x = 30,y = 20)

B2 = Button(top, text = "Close Gripper", command = close)
B2.place(x = 160,y = 20)

top.mainloop()