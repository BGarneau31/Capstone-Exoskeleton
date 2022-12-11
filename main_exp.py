import csv
import time
from tkinter import *
from PIL import Image, ImageTk
import customtkinter
from customtkinter import *
import turtle
from PythonArduino import PythonArduino

# calibrate function then run trial creates issue that closes GUI? - next semester issue

customtkinter.set_appearance_mode("system")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green
LEFT = (-450*2, 0)
RIGHT = (450*2, 0)
CLOSE_LEFT = (-225*2, 0)
CLOSE_RIGHT = (225*2, 0)
now = time.ctime()
print("Current Time:", now)


class RootWindow:

    def __init__(self, master):
        self.patientWindow = PatientWindow()  # opens patient window
        self.arduino_data = PythonArduino()  # pull in arduino data object
        self.position = None
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

        speed_label = customtkinter.CTkLabel(self.frame_left, text='Speed Setting:')
        speed_label.grid(row=5, column=0, columnspan=2, pady=(20, 0))
        self.speed_var = customtkinter.StringVar()
        speed_slider = customtkinter.CTkComboBox(self.frame_left, variable=self.speed_var, values=['Slow', 'Fast'], state='normal', command=self.update_speed)
        speed_slider.grid(row=6, column=0, columnspan=2, padx=10, pady=20)

        self.run_trial_but = customtkinter.CTkButton(self.frame_left, text="Run Trial", command=self.run_trial, fg_color="green")
        self.run_trial_but.grid(row=7, column=0, columnspan=2, padx=10, pady=20)

        self.frame_left.grid(padx=40, pady=50, row=0, column=0)

        # right frame
        self.frame_right = customtkinter.CTkFrame(master)

        close_left_but = customtkinter.CTkButton(self.frame_right, text="Go Close Left", command=self.go_close_left)
        close_left_but.grid(padx=50, pady=20, row=0, column=0)

        far_left_but = customtkinter.CTkButton(self.frame_right, text="Go Far Left", command=self.go_far_left)
        far_left_but.grid(padx=50, pady=20, row=1, column=0)

        close_right_but = customtkinter.CTkButton(self.frame_right, text="Go Close Right", command=self.go_close_right)
        close_right_but.grid(padx=50, pady=20, row=0, column=1)

        far_right_but = customtkinter.CTkButton(self.frame_right, text="Go Far Right", command=self.go_far_right)
        far_right_but.grid(padx=50, pady=20, row=1, column=1)

        center_but = customtkinter.CTkButton(self.frame_right, text="Go to Center", command=self.go_to_center)
        center_but.grid(padx=50, pady=20, row=3, column=0, columnspan=2)

        calibrate_but = customtkinter.CTkButton(self.frame_right, text="Calibrate", command=self.calibrate)
        calibrate_but.grid(padx=50, pady=20, row=4, column=0, columnspan=2)

        stop_but = customtkinter.CTkButton(self.frame_right, text="Stop Trial", command=self.stop_trial, fg_color="red")
        stop_but.grid(padx=50, pady=20, row=5, column=0, columnspan=2)

        self.frame_right.grid(padx=20, pady=50, row=0, column=1)

    # Root Window Functions

    def open(self):  # toplevel window now created first when program run, so this function is depreciated
        self.patientWindow = PatientWindow()

    def update_user_data(self):
        # update csv file with user number and trial num
        # uses .get() with entry text variables
        trial_data = [self.user_entry_var.get(), self.trial_entry_var.get()]
        with open('exo_data.csv', 'w') as file:
            writer = csv.writer(file)
            writer.writerow(['User Number ', 'Trial Number'])

            writer.writerow(trial_data)
        print("User and Trial Data Collected")

    def record_data(self):
        # update bool value to update "data collection" function that will take some type of data (eeg,emg)
        pass

    def run_trial(self):
        # need delay or wait till command between each left/right command
        # time.sleep(1)
        self.go_close_left()
        if self.position == 'at left1 position':
            self.go_far_left()
        else:
            self.stop_trial()
        if self.position == 'at left2 position':
            self.go_close_left()
        else:
            self.stop_trial()
        if self.position == 'at left1 position':
            self.go_to_center()
        else:
            self.stop_trial()
        if self.position == 'at home position':
            self.go_close_right()
        else:
            self.stop_trial()

        if self.position == 'at right1 position':
            self.go_far_right()
        else:
            self.stop_trial()

        if self.position == 'at right2 position':
            self.go_close_right()
        else:
            self.stop_trial()

        if self.position == 'at right1 position':
            self.go_to_center()
        else:
            self.stop_trial()

        self.patientWindow.good_job_img()

        # self.go_close_left()
        # self.go_far_left()
        # self.go_close_left()
        # self.go_to_center()
        # self.go_close_right()
        # self.go_far_right()
        # self.go_close_right()
        # self.go_to_center()
        # self.patientWindow.good_job_img()

        print("Trial Done")

    def stop_trial(self):
        self.arduino_data.send_data("stop")  # will need to update this with actual code command to send to kill the motor
        self.patientWindow.destroy_patient_window()

    def update_speed(self, speed):
        if self.speed_var.get() == "Slow":
            self.patientWindow.user_turtle.speed(1)
            self.patientWindow.screen.delay(32)
        if self.speed_var.get() == "Medium":
            self.patientWindow.user_turtle.speed(1)
            self.patientWindow.screen.delay(100)
        if self.speed_var.get() == "Fast":
            self.patientWindow.user_turtle.speed(1)
            self.patientWindow.screen.delay(17)
        print(self.speed_var.get())

    def set_heading(self, direction):
        self.patientWindow.user_turtle.speed(10)
        self.patientWindow.screen.delay(0)
        self.patientWindow.user_turtle.setheading(direction)
        self.update_speed(self.speed_var.get())

    def go_to_center(self):
        if self.speed_var.get() == "Slow":
            self.arduino_data.send_data(f"00")
            time.sleep(1*.5)
        else:
            self.arduino_data.send_data(f"01")
            time.sleep(1*.5)
        self.patientWindow.show_center_wall()
        if self.patientWindow.user_turtle.xcor() < 1:
            self.patientWindow.right_arrow()
            self.set_heading(0)
        if self.patientWindow.user_turtle.xcor() > 1:
            self.patientWindow.left_arrow()
            self.set_heading(180)
        self.patientWindow.user_turtle.goto((0, 0))
        self.position = self.arduino_data.receive_data()
        print(self.position)

    def go_close_left(self):
        if self.speed_var.get() == "Slow":
            self.arduino_data.send_data(f"10")
            time.sleep(1*.5)
        else:
            self.arduino_data.send_data(f"11")
            time.sleep(1*.5)
        self.patientWindow.show_left_wall_close()
        if self.patientWindow.user_turtle.xcor() > -225*2:
            self.patientWindow.left_arrow()
            self.set_heading(180)
        else:
            self.patientWindow.right_arrow()
            self.set_heading(0)
        self.patientWindow.user_turtle.goto(CLOSE_LEFT)
        self.position = self.arduino_data.receive_data()
        print(self.position)

    def go_close_right(self):
        if self.speed_var.get() == "Slow":
            self.arduino_data.send_data(f"30")
            time.sleep(1*.5)
        else:
            self.arduino_data.send_data(f"31")
            time.sleep(1*.5)
        self.patientWindow.show_right_wall_close()
        if self.patientWindow.user_turtle.xcor() < 225*2:
            self.patientWindow.right_arrow()
            self.set_heading(0)
        else:
            self.patientWindow.left_arrow()
            self.set_heading(180)
        self.patientWindow.user_turtle.goto(CLOSE_RIGHT)
        self.position = self.arduino_data.receive_data()
        print(self.position)

    def go_far_left(self):
        if self.speed_var.get() == "Slow":
            self.arduino_data.send_data(f"20")
            time.sleep(1*.5)
        else:
            self.arduino_data.send_data(f"21")
            time.sleep(1*.5)
        self.patientWindow.show_left_wall()
        self.patientWindow.left_arrow()
        self.set_heading(180)
        self.patientWindow.user_turtle.goto(LEFT)
        self.position = self.arduino_data.receive_data()
        print(self.position)

    def go_far_right(self):
        if self.speed_var.get() == "Slow":
            self.arduino_data.send_data(f"40")
            time.sleep(1*.5)
        else:
            self.arduino_data.send_data(f"41")
            time.sleep(1*.5)
        self.patientWindow.show_right_wall()
        self.patientWindow.right_arrow()
        self.set_heading(0)
        self.patientWindow.user_turtle.goto(RIGHT)
        self.position = self.arduino_data.receive_data()
        print(self.position)

    def calibrate(self):
        self.arduino_data.send_data("01")
        # time.sleep(5)
        self.patientWindow.please_wait()
        self.patientWindow.hide_all_walls()
        self.patientWindow.user_turtle.speed(10)
        self.patientWindow.user_turtle.home()
        self.position = self.arduino_data.receive_data()
        print(self.position)


class PatientWindow:
    def __init__(self):

        self.top = customtkinter.CTkToplevel()
        self.top.geometry("%dx%d+%d+%d" % (700, 625, 2700, 50))  # old was 1050, 900, 2350, 50
        self.top.title("Exoskeleton Patient View")

        # Top Frame
        w = 1050*2
        h = 450*2

        self.frame_top = customtkinter.CTkFrame(self.top)
        self.canvas = Canvas(self.frame_top, width=w, height=h, bg='gray')
        self.canvas.grid(row=0, column=0)
        self.frame_top.grid(row=0, column=0)

        # Bottom Frame
        self.frame_bottom = customtkinter.CTkFrame(self.top)

        im = Image.open("images/please-wait2.png")
        resized = im.resize((600*2, 400*2), Image.Resampling.LANCZOS)
        ph = ImageTk.PhotoImage(resized)

        self.label = Label(self.frame_bottom, image=ph, width=600*2, height=400*2)
        self.label.image = ph  # need to keep the reference of your image to avoid garbage collection
        self.label.grid(row=1, column=0)
        self.frame_bottom.grid(row=1, column=0, pady=20)

        # Turtle Canvas and Turtle Objects
        self.screen = turtle.TurtleScreen(self.canvas)
        self.screen.bgcolor("cyan")
        self.user_turtle = turtle.RawTurtle(self.screen, shape='turtle')
        self.user_turtle.shapesize(stretch_len=4, stretch_wid=4)
        self.user_turtle.color("green")
        self.user_turtle.penup()

        self.center_wall = turtle.RawTurtle(self.screen, shape="circle")
        self.center_wall.hideturtle()
        self.center_wall.shapesize(stretch_len=5, stretch_wid=5)
        self.center_wall.color("light green")
        self.center_wall.penup()

        self.left_wall = turtle.RawTurtle(self.screen, shape="square")
        self.left_wall.hideturtle()
        self.left_wall.shapesize(stretch_len=3, stretch_wid=15)
        self.left_wall.color("saddle brown")
        self.left_wall.penup()
        self.left_wall.setx(-450*2)

        self.right_wall = turtle.RawTurtle(self.screen, shape="square")
        self.right_wall.hideturtle()
        self.right_wall.shapesize(stretch_len=3, stretch_wid=15)
        self.right_wall.color("saddle brown")
        self.right_wall.penup()
        self.right_wall.setx(450*2)

        self.left_wall_close = turtle.RawTurtle(self.screen, shape="square")
        self.left_wall_close.hideturtle()
        self.left_wall_close.shapesize(stretch_len=3, stretch_wid=15)
        self.left_wall_close.color("saddle brown")
        self.left_wall_close.penup()
        self.left_wall_close.setx(-225*2)

        self.right_wall_close = turtle.RawTurtle(self.screen, shape="square")
        self.right_wall_close.hideturtle()
        self.right_wall_close.shapesize(stretch_len=3, stretch_wid=15)
        self.right_wall_close.color("saddle brown")
        self.right_wall_close.penup()
        self.right_wall_close.setx(225*2)

    # Top Level Window Functions

    def show_right_wall(self):
        self.center_wall.hideturtle()
        self.left_wall.hideturtle()
        self.right_wall_close.hideturtle()
        self.left_wall_close.hideturtle()
        self.right_wall.showturtle()

    def show_right_wall_close(self):
        self.center_wall.hideturtle()
        self.left_wall.hideturtle()
        self.left_wall_close.hideturtle()
        self.right_wall.hideturtle()
        self.right_wall_close.showturtle()

    def show_left_wall(self):
        self.right_wall.hideturtle()
        self.center_wall.hideturtle()
        self.right_wall_close.hideturtle()
        self.left_wall_close.hideturtle()
        self.left_wall.showturtle()

    def show_left_wall_close(self):
        self.center_wall.hideturtle()
        self.left_wall.hideturtle()
        self.right_wall_close.hideturtle()
        self.right_wall.hideturtle()
        self.left_wall_close.showturtle()

    def show_center_wall(self):
        self.right_wall.hideturtle()
        self.left_wall.hideturtle()
        self.left_wall_close.hideturtle()
        self.right_wall_close.hideturtle()
        self.center_wall.showturtle()

    def hide_all_walls(self):
        self.right_wall.hideturtle()
        self.left_wall.hideturtle()
        self.left_wall_close.hideturtle()
        self.right_wall_close.hideturtle()
        self.center_wall.hideturtle()

    # function to update speed of turtle object
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

    # function to update images for patient commands
    def stop_image(self):
        stop_img = Image.open("images/stop.gif")
        stop_img_resized = stop_img.resize((600*2, 400*2), Image.Resampling.LANCZOS)
        photo_img = ImageTk.PhotoImage(stop_img_resized)
        self.label.config(image=photo_img)
        self.label.image = photo_img

    def right_arrow(self):
        right_img = Image.open("images/green right arrow.png")
        right_img_resized = right_img.resize((600*2, 400*2), Image.Resampling.LANCZOS)
        photo_img = ImageTk.PhotoImage(right_img_resized)
        self.label.config(image=photo_img)
        self.label.image = photo_img

    def left_arrow(self):
        left_img = Image.open("images/green left arrow.png")
        left_img_resized = left_img.resize((600*2, 400*2), Image.Resampling.LANCZOS)
        photo_img = ImageTk.PhotoImage(left_img_resized)
        self.label.config(image=photo_img)
        self.label.image = photo_img

    def please_wait(self):
        wait_img = Image.open("images/please-wait.png")
        wait_img_resized = wait_img.resize((600*2, 400*2), Image.Resampling.LANCZOS)
        photo_img = ImageTk.PhotoImage(wait_img_resized)
        self.label.config(image=photo_img)
        self.label.image = photo_img

    def good_job_img(self):
        good_img = Image.open("images/good_job.jpg")
        good_img_resized = good_img.resize((600*2, 400*2), Image.Resampling.LANCZOS)
        photo_img = ImageTk.PhotoImage(good_img_resized)
        self.label.config(image=photo_img)
        self.label.image = photo_img

    def destroy_patient_window(self):
        self.top.destroy()
        self.top.update()


if __name__ == "__main__":
    root = CTk()
    root.geometry("%dx%d+%d+%d" % (920, 500, 300, 300))
    root.title("Exoskeleton Technician Controls")
    main_window = RootWindow(root)
    root.mainloop()
