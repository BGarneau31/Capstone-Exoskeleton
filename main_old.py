import csv
import time
import turtle
from tkinter import *
from PIL import Image, ImageTk
import customtkinter
from customtkinter import *
import turtle
from turtle import *
from PythonArduino import TestFakeArduino

customtkinter.set_appearance_mode("system")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green
LEFT = (-245, 0)
RIGHT = (245, 0)

class RootWindow():

    def __init__(self, master):

        # self.patientWindow = None
        self.arduino_data = TestFakeArduino()

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

        button2 = customtkinter.CTkButton(self.frame_right, text="Update Image to Right", command=self.go_right)
        button2.grid(padx=50, pady=20, row=0, column=0)

        button3 = customtkinter.CTkButton(self.frame_right, text="Update Image to Left", command=self.go_left)
        button3.grid(padx=50, pady=20, row=1, column=0)

        button3 = customtkinter.CTkButton(self.frame_right, text="Update Image to Stop", command=self.stop_image)
        button3.grid(padx=50, pady=20, row=2, column=0)

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
        # must calibrate before so maybe grey it out until calibrate is run?
        # confirm at center
        # select speed, gray out run trail until speed selected
        # go left, show left image, delay/wait
        # wait for sensor to say "at left", since at left and need to go to center, show right image
        # go right to center
        # wait for sensor
        # go right
        # wait for sensor
        # go left to center
        # wait for sensor to say center
        # stop
        self.update_speed(self.speed_var.get())
        self.patientWindow.left_arrow()
        self.go_left()
        # need delay or wait till command
        # time.sleep(1)
        self.patientWindow.right_arrow()
        self.go_to_center()
        self.patientWindow.right_arrow()
        # need delay or wait till command
        self.go_right()
        # need delay or wait till command
        self.patientWindow.left_arrow()
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




    def stop_image(self):
        if self.arduino_data.receive_data() == "at sensor":
            self.patientWindow.stop_image()

    def calibrate(self):
        # send command to motor to go to center
        # if self.arduino_data.receive_data() == 0:
            self.patientWindow.please_wait()
            self.patientWindow.user_turtle.speed(10)
            self.patientWindow.user_turtle.home()



class PatientWindow():
    def __init__(self):

        self.top = customtkinter.CTkToplevel()
        self.top.geometry("600x850")
        self.top.title("Exoskeleton Patient View")
        self.frame = customtkinter.CTkFrame(self.top)

        im = Image.open("images/please-wait2.png")
        resized = im.resize((600, 600), Image.Resampling.LANCZOS)
        ph = ImageTk.PhotoImage(resized)

        self.label = Label(self.frame, image=ph, width=600, height=600)
        self.label.image = ph  # need to keep the reference of your image to avoid garbage collection
        self.label.grid(row=0, column=0)
        self.frame.grid(row=0, column=0)

        w = 600
        h = 250

        self.frame_bottom = customtkinter.CTkFrame(self.top)
        self.canvas = Canvas(self.frame_bottom, width=w, height=h, bg='gray')
        self.canvas.grid(row=0, column=0)

        x = w // 2
        y = h // 2
        cursor = self.canvas.create_oval(x, y, x+10, y+10, fill='red')

        # left_wall = self.canvas.create_rectangle(125, 90, 100, 165, fill='pink')

        self.frame_bottom.grid(row=1, column=0)

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

    def show_right_wall(self):
        self.left_wall.hideturtle()
        self.right_wall.showturtle()
        self.user_turtle.setheading(0)

    def show_left_wall(self):
        self.right_wall.hideturtle()
        self.left_wall.showturtle()
        # self.user_turtle.setheading(180)

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
        stop_img_resized = stop_img.resize((600, 600), Image.Resampling.LANCZOS)
        photo_img = ImageTk.PhotoImage(stop_img_resized)
        self.label.config(image=photo_img)
        self.label.image = photo_img

    def right_arrow(self):
        right_img = Image.open("images/right-arrow.gif")
        right_img_resized = right_img.resize((600, 600), Image.Resampling.LANCZOS)
        photo_img = ImageTk.PhotoImage(right_img_resized)
        self.label.config(image=photo_img)
        self.label.image = photo_img

    def left_arrow(self):
        left_img = Image.open("images/left-arrow.gif")
        left_img_resized = left_img.resize((600, 600), Image.Resampling.LANCZOS)
        photo_img = ImageTk.PhotoImage(left_img_resized)
        self.label.config(image=photo_img)
        self.label.image = photo_img

    def please_wait(self):
        wait_img = Image.open("images/please-wait.png")
        wait_img_resized = wait_img.resize((600, 600), Image.Resampling.LANCZOS)
        photo_img = ImageTk.PhotoImage(wait_img_resized)
        self.label.config(image=photo_img)
        self.label.image = photo_img

    def good_job_img(self):
        good_img = Image.open("images/good_job.jpg")
        good_img_resized = good_img.resize((600, 600), Image.Resampling.LANCZOS)
        photo_img = ImageTk.PhotoImage(good_img_resized)
        self.label.config(image=photo_img)
        self.label.image = photo_img

    def destroy_patient_window(self):
        self.top.destroy()
        self.top.update()


if __name__ == "__main__":
    root = CTk()
    root.geometry("690x500")
    root.title("Exoskeleton Technician Controls")
    main_window = RootWindow(root)
    root.mainloop()
