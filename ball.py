import tkinter as tk
from tkinter import Canvas, messagebox
from tkinter import ttk
from tkinter import *
from turtle import bgcolor

root = Tk()
root.title('Ball Game')
root.geometry('800x600')

w = 600
h = 400
x = w // 2
y = h // 2

canvas = Canvas(root, width=w, height=h, bg="black")
canvas.pack(pady=50)

circle = canvas.create_oval(x, y, x + 10, y + 10, fill='white')


def left(event):
    x = -10
    y = 0
    canvas.move(circle, x, y)


def right(event):
    x = 10
    y = 0
    canvas.move(circle, x, y)


def down(event):
    x = 0
    y = 10
    canvas.move(circle, x, y)


def up(event):
    x = 0
    y = -10
    canvas.move(circle, x, y)


root.bind("<Left>", left)
root.bind("<Right>", right)
root.bind("<Up>", up)
root.bind("<Down>", down)

root.mainloop()