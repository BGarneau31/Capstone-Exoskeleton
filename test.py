import csv
import time
import turtle
from tkinter import *
from PIL import Image, ImageTk
import customtkinter
from customtkinter import *
import turtle
from turtle import *
from PythonArduinoCode import TestFakeArduino

customtkinter.set_appearance_mode("system")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green
LEFT = (-245, 0)
RIGHT = (245, 0)


class RootWindow():

    def __init__(self, master):
        self.patientWindow = None
        self.arduino_data = TestFakeArduino()  # pull in arduino data object

        # left frame
        self.frame_left = customtkinter.CTkFrame(master)

        button1 = customtkinter.CTkButton(self.frame_left, text="Open Patient Window", command=self.open)
        button1.grid(row=0, column=0, columnspan=2, padx=10, pady=20)

        user_label = customtkinter.CTkLabel(self.frame_left, text='User Number:')
        user_label.grid(row=1, column=0,)
        self.user_entry_var = customtkinter.StringVar()
        user_entry = customtkinter.CTkEntry(self.frame_left, textvariable=self.user_entry_var)
        user_entry.grid(row=1, column=1, padx=10)

        trial_label = customtkinter.CTkLabel(self.frame_left, text='Trial Number:')
        trial_label.grid(row=2, column=0)
        self.trial_entry_var = customtkinter.StringVar()
        trial_entry = customtkinter.CTkEntry(self.frame_left, textvariable=self.trial_entry_var)
        trial_entry.grid(row=2, column=1, padx=10)

        button1 = customtkinter.CTkButton(self.frame_left, text="Submit User/Trial Data", command=self.update_user_data)
        button1.grid(row=3, column=0, columnspan=2, padx=10, pady=20)

        collect_data_box = customtkinter.CTkCheckBox(self.frame_left, text="Record Data", command=self.record_data)
        collect_data_box.grid(row=4, column=0, columnspan=2, padx=50, pady=10)

        self.run_trial_but = customtkinter.CTkButton(self.frame_left, text="Run Trial", command=self.run_trial)
        self.run_trial_but.grid(row=5, column=0, columnspan=2, padx=10, pady=20)

        self.frame_left.grid(padx=40, pady=50, row=0, column=0)

        # right frame
        self.frame_right = customtkinter.CTkFrame(master)

        close_left_but = customtkinter.CTkButton(self.frame_right, text="Go Close Left", command=self.go_close_left)
        close_left_but.grid(padx=50, pady=20, row=0, column=0)

        close_right_but = customtkinter.CTkButton(self.frame_right, text="Go Close Right", command=self.go_close_right)
        close_right_but.grid(padx=50, pady=20, row=1, column=0)

        far_left_but = customtkinter.CTkButton(self.frame_right, text="Go Far Left", command=self.go_far_left)
        far_left_but.grid(padx=50, pady=20, row=2, column=0)

        far_right_but = customtkinter.CTkButton(self.frame_right, text="Go Far Right", command=self.go_far_right)
        far_right_but.grid(padx=50, pady=20, row=2, column=0)

        calibrate_but = customtkinter.CTkButton(self.frame_right, text="Calibrate", command=self.calibrate)
        calibrate_but.grid(padx=50, pady=20, row=3, column=0)

        stop_but = customtkinter.CTkButton(self.frame_right, text="Stop Trial", command=self.stop_trial)
        stop_but.grid(padx=50, pady=20, row=4, column=0)

        speed_label = customtkinter.CTkLabel(self.frame_right, text='Speed Setting:')
        speed_label.grid(row=5, column=0)
        self.speed_var = customtkinter.StringVar()
        speed_slider = customtkinter.CTkComboBox(self.frame_right, variable=self.speed_var, values=['Slow', 'Medium', 'Fast'], state='normal', command=self.update_speed)
        speed_slider.grid(row=6, column=0, pady=(0,20))

        self.frame_right.grid(padx=20, pady=50, row=0, column=1)

    # Root Window Functions

    def open(self):
        self.patientWindow = PatientWindow()

    def update_user_data(self):
        # update csv file with user number and trial num
        # uses .get() with entry text variables
        trial_data = [self.user_entry_var.get(), self.trial_entry_var.get()]
        with open('exo_data.csv','w') as file:
            writer = csv.writer(file)
            writer.writerow(['User Number', 'Trial Number'])

            writer.writerow(trial_data)
        print("User and Trial Data Collected")

    def record_data(self):
        # update bool value to update "data collection" function that will take some type of data (eeg,emg)
        pass

    def run_trial(self):
        # need delay or wait till command between each left/right command
        # time.sleep(1)

        self.patientWindow.left_arrow()
        self.set_heading(180)
        self.go_left()

        self.patientWindow.right_arrow()
        self.set_heading(0)
        self.go_to_center()

        self.patientWindow.right_arrow()
        self.go_right()

        self.patientWindow.left_arrow()
        self.set_heading(180)
        self.go_to_center()

        self.patientWindow.good_job_img()

        print("Trial Done")

    def stop_trial(self):
        self.patientWindow.destroy_patient_window()

    def update_speed(self, speed):
        if self.speed_var.get() == "Slow":
            self.patientWindow.user_turtle.speed(1)
            self.patientWindow.screen.delay(300)
        if self.speed_var.get() == "Medium":
            self.patientWindow.user_turtle.speed(1)
            self.patientWindow.screen.delay(100)
        if self.speed_var.get() == "Fast":
            self.patientWindow.user_turtle.speed(1)
            self.patientWindow.screen.delay(30)
        print(self.speed_var.get())

    def set_heading(self, direction):
        self.patientWindow.user_turtle.speed(10)
        self.patientWindow.user_turtle.setheading(direction)
        self.update_speed(self.speed_var.get())

    def go_right(self):
        # if self.arduino_data.receive_data() == "go right":
        #     self.patientWindow.right_arrow()
            self.patientWindow.show_right_wall()
            # self.update_speed(self.speed_var.get())
            self.patientWindow.user_turtle.goto(RIGHT)

    def go_left(self):
        # if self.arduino_data.receive_data() == "go left":
        #     self.patientWindow.left_arrow()
            self.patientWindow.show_left_wall()
            # self.update_speed(self.speed_var.get())
            self.patientWindow.user_turtle.goto(LEFT)

    def go_to_center(self):
        # if self.arduino_data.receive_data() == "center":
            self.patientWindow.show_center_wall()
            # self.update_speed(self.speed_var.get())
            # if self.arudino_data_position() == "at left":
            # if self.patientWindow.user_turtle.pos == RIGHT:
            #     self.patientWindow.left_arrow()
            #     self.patientWindow.user_turtle.home()
            # else:
            #     self.patientWindow.right_arrow()
            self.patientWindow.user_turtle.home()

    def go_close_left(self):
        self.arduino_data.send_data(f"close left {specifc_speed}")  # need to change the string and speed to be read
        pass

    def go_close_right(self):
        self.arduino_data.send_data(f"close right {specifc_speed}")
        pass

    def go_far_left(self):
        self.arduino_data.send_data(f"far left {specifc_speed}")
        pass

    def go_far_right(self):
        self.arduino_data.send_data(f"far left {specifc_speed}")
        pass

    def calibrate(self):
        self.arduino_data.send_data("center 00") # arduino takes location and speed command
        time.sleep(5)
        # if self.arduino_data.receive_data() == "at center":
            self.patientWindow.please_wait()
            self.patientWindow.user_turtle.speed(10)
            self.patientWindow.user_turtle.home()


class PatientWindow():
    def __init__(self):

        self.top = customtkinter.CTkToplevel()
        self.top.geometry("%dx%d+%d+%d" % (1050, 900, 2300, 50))
        self.top.title("Exoskeleton Patient View")

        # Top Frame
        w = 1050
        h = 450

        self.frame_top = customtkinter.CTkFrame(self.top)
        self.canvas = Canvas(self.frame_top, width=w, height=h, bg='gray')
        self.canvas.grid(row=0, column=0)
        x = w // 2
        y = h // 2
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
        self.user_turtle.shapesize(stretch_len=1, stretch_wid=1)
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
        self.left_wall.setx(-250)

        self.right_wall = turtle.RawTurtle(self.screen, shape="square")
        self.right_wall.hideturtle()
        self.right_wall.shapesize(stretch_len=1, stretch_wid=5)
        self.right_wall.color("saddle brown")
        self.right_wall.penup()
        self.right_wall.setx(250)

        self.left_wall_close = turtle.RawTurtle(self.screen, shape="square")
        self.left_wall_close.hideturtle()
        self.left_wall_close.shapesize(stretch_len=1, stretch_wid=5)
        self.left_wall_close.color("saddle brown")
        self.left_wall_close.penup()
        self.left_wall_close.setx(-125)

        self.right_wall_close = turtle.RawTurtle(self.screen, shape="square")
        self.right_wall_close.hideturtle()
        self.right_wall_close.shapesize(stretch_len=1, stretch_wid=5)
        self.right_wall_close.color("saddle brown")
        self.right_wall_close.penup()
        self.right_wall_close.setx(125)

    # Top Level Window Functions

    def show_right_wall(self):
        self.left_wall.hideturtle()
        self.right_wall.showturtle()

    def show_left_wall(self):
        self.right_wall.hideturtle()
        self.left_wall.showturtle()

    def show_center_wall(self):
        self.right_wall.hideturtle()
        self.left_wall.hideturtle()
        self.center_wall.showturtle()

    def set_turtle_speed(self, speed):
        # take in info related to selected GUI speed and call function that sends data to arduino in PythonArduinoCode
        if speed == "Slow":
            self.user_turtle.speed(1)
            self.screen.delay(300)
        if speed == "Medium":
            self.user_turtle.speed(1)
            self.screen.delay(100)
        if speed == "Fast":
            self.user_turtle.speed(1)
            self.screen.delay(30)

    def stop_image(self):
        stop_img = Image.open("images/stop.gif")
        stop_img_resized = stop_img.resize((600, 400), Image.Resampling.LANCZOS)
        photo_img = ImageTk.PhotoImage(stop_img_resized)
        self.label.config(image=photo_img)
        self.label.image = photo_img

    def right_arrow(self):
        right_img = Image.open("images/right-arrow.gif")
        right_img_resized = right_img.resize((600, 400), Image.Resampling.LANCZOS)
        photo_img = ImageTk.PhotoImage(right_img_resized)
        self.label.config(image=photo_img)
        self.label.image = photo_img

    def left_arrow(self):
        left_img = Image.open("images/left-arrow.gif")
        left_img_resized = left_img.resize((600, 400), Image.Resampling.LANCZOS)
        photo_img = ImageTk.PhotoImage(left_img_resized)
        self.label.config(image=photo_img)
        self.label.image = photo_img

    def please_wait(self):
        wait_img = Image.open("images/please-wait.png")
        wait_img_resized = wait_img.resize((600, 400), Image.Resampling.LANCZOS)
        photo_img = ImageTk.PhotoImage(wait_img_resized)
        self.label.config(image=photo_img)
        self.label.image = photo_img

    def good_job_img(self):
        good_img = Image.open("images/good_job.jpg")
        good_img_resized = good_img.resize((600, 400), Image.Resampling.LANCZOS)
        photo_img = ImageTk.PhotoImage(good_img_resized)
        self.label.config(image=photo_img)
        self.label.image = photo_img

    def destroy_patient_window(self):
        self.top.destroy()
        self.top.update()


if __name__ == "__main__":
    root = CTk()
    root.geometry("%dx%d+%d+%d" % (690, 500, 300, 300))
    root.title("Exoskeleton Technician Controls")
    main_window = RootWindow(root)
    root.mainloop()
