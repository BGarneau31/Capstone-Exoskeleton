# main_window file - keeps most of test_main.py
# supporting window creation files - take patient window class in test_main and put here
# all specific window functions will be here under specified if statements? or can make this file more general and have the functions somewhere else

import customtkinter
from customtkinter import *
from tkinter import *


class WindowCreation():

    def __init__(self, title):
        self.top = customtkinter.CTkToplevel()
        self.top.geometry("%dx%d+%d+%d" % (1050, 900, 0, 0))
        self.top.title(title)

        if title == "Planar Exoskeleton Window":

            w = 1050
            h = 450

            self.frame_top = customtkinter.CTkFrame(self.top)
            self.canvas = Canvas(self.frame_top, width=w, height=h, bg='gray')
            self.canvas.grid(row=0, column=0)
            self.frame_top.grid(row=0, column=0)

        elif title == "Exo Glove Window":
            w = 500
            h = 500

            self.frame_top = customtkinter.CTkFrame(self.top)
            self.canvas = Canvas(self.frame_top, width=w, height=h, bg='gray')
            self.canvas.grid(row=0, column=0)
            self.frame_top.grid(row=0, column=0)