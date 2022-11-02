from main import *

from tkinter import *
from PIL import Image, ImageTk
import customtkinter
from customtkinter import *
from turtle import Turtle

# customtkinter.set_appearance_mode("system")  # Modes: system (default), light, dark
# customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

if __name__ == "__main__":
    root = CTk()
    root.geometry("690x500")
    root.title("Exoskeleton Technician Controls")
    root_window = RootWindow(root)
    root.mainloop()
