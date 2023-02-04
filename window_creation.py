# main_window file - keeps most of test_main.py
# supporting window creation files - take patient window class in test_main and put here
# all specific window functions will be here under specified if statements? or can make this file more general and have the functions somewhere else

import customtkinter
from customtkinter import *
from tkinter import *
import turtle
from PIL import Image, ImageTk


class PlanarWindowCreation():

    def __init__(self, *args, **kwargs):
        self.top = CTkToplevel()
        self.top.geometry("%dx%d+%d+%d" % (1050, 900, 0, 0))
        self.top.title("Exo Planar Window")

        # Top Frame
        w = 1050
        h = 450

        self.frame_top = customtkinter.CTkFrame(self.top)
        self.canvas = Canvas(self.frame_top, width=w, height=h, bg='gray')
        self.canvas.grid(row=0, column=0)
        self.frame_top.grid(row=0, column=0)

        # Bottom Frame
        self.frame_bottom = customtkinter.CTkFrame(self.top)

        im = Image.open("images/please-wait2.png")
        resized = im.resize((600, 400), Image.Resampling.LANCZOS)
        ph = ImageTk.PhotoImage(resized)

        self.label = Label(self.frame_bottom, image=ph, width=600, height=400)
        self.label.image = ph  # need to keep the reference of your image to avoid garbage collection
        self.label.grid(row=1, column=0)
        self.frame_bottom.grid(row=1, column=0, pady=20)

        # Turtle Canvas and Turtle Objects
        self.screen = turtle.TurtleScreen(self.canvas)
        self.screen.bgcolor("cyan")
        self.user_turtle = turtle.RawTurtle(self.screen, shape='turtle')
        self.user_turtle.shapesize(stretch_len=2, stretch_wid=2)
        self.user_turtle.color("green")
        self.user_turtle.penup()

        self.center_wall = turtle.RawTurtle(self.screen, shape="circle")
        self.center_wall.hideturtle()
        self.center_wall.shapesize(stretch_len=2, stretch_wid=2)
        self.center_wall.color("light green")
        self.center_wall.penup()

        self.left_wall = turtle.RawTurtle(self.screen, shape="square")
        self.left_wall.hideturtle()
        self.left_wall.shapesize(stretch_len=1, stretch_wid=5)
        self.left_wall.color("saddle brown")
        self.left_wall.penup()
        self.left_wall.setx(-450)

        self.right_wall = turtle.RawTurtle(self.screen, shape="square")
        self.right_wall.hideturtle()
        self.right_wall.shapesize(stretch_len=1, stretch_wid=5)
        self.right_wall.color("saddle brown")
        self.right_wall.penup()
        self.right_wall.setx(450)

        self.left_wall_close = turtle.RawTurtle(self.screen, shape="square")
        self.left_wall_close.hideturtle()
        self.left_wall_close.shapesize(stretch_len=1, stretch_wid=5)
        self.left_wall_close.color("saddle brown")
        self.left_wall_close.penup()
        self.left_wall_close.setx(-225)

        self.right_wall_close = turtle.RawTurtle(self.screen, shape="square")
        self.right_wall_close.hideturtle()
        self.right_wall_close.shapesize(stretch_len=1, stretch_wid=5)
        self.right_wall_close.color("saddle brown")
        self.right_wall_close.penup()
        self.right_wall_close.setx(225)

    def close_window(self):
        self.top.destroy()


class GloveWindowCreation():

    def __init__(self, *args, **kwargs):
        self.top2 = CTkToplevel()
        self.top2.geometry("%dx%d+%d+%d" % (500, 500, 0, 0))
        self.top2.title("Exo Glove Window")

        self.canvas = Canvas(self.top2, width=500, height=500, bg='gray', highlightthickness=0)
        self.canvas.grid(row=0, column=0)

        im = Image.open("images/please-wait2.png")
        resized = im.resize((500, 500), Image.Resampling.LANCZOS)
        ph = ImageTk.PhotoImage(resized)

        self.label = Label(self.canvas, image=ph, width=500, height=500, borderwidth=0)
        self.label.image = ph  # need to keep the reference of your image to avoid garbage collection
        self.label.grid(row=1, column=0)

    def open_hand_image(self):
        good_img = Image.open("images/open_hand.jpg")
        good_img_resized = good_img.resize((500,500), Image.Resampling.LANCZOS)
        photo_img = ImageTk.PhotoImage(good_img_resized)
        self.label.config(image=photo_img)
        self.label.image = photo_img

    def close_hand_image(self):
        good_img = Image.open("images/close_hand.jpg")
        good_img_resized = good_img.resize((500,500), Image.Resampling.LANCZOS)
        photo_img = ImageTk.PhotoImage(good_img_resized)
        self.label.config(image=photo_img)
        self.label.image = photo_img

    def good_job_img(self):
        good_img = Image.open("images/good_job.jpg")
        good_img_resized = good_img.resize((500, 500), Image.Resampling.LANCZOS)
        photo_img = ImageTk.PhotoImage(good_img_resized)
        self.label.config(image=photo_img)
        self.label.image = photo_img

    def close_window(self):
        self.top2.destroy()





