from tkinter import *
from PIL import Image, ImageTk
import customtkinter
from customtkinter import *
from turtle import Turtle

customtkinter.set_appearance_mode("system")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green


class RootWindow():

    def __init__(self, master):

        self.patientWindow = None
        # left frame
        self.frame_left = customtkinter.CTkFrame(master)

        button1 = customtkinter.CTkButton(self.frame_left, text="Open Patient Window", command=self.open)
        button1.grid(row=0, column=0, columnspan=2, padx=10, pady=20)

        user_label = customtkinter.CTkLabel(self.frame_left, text='User Number:')
        user_label.grid(row=1, column=0,)
        user_entry_var = customtkinter.StringVar()
        user_entry = customtkinter.CTkEntry(self.frame_left, textvariable=user_entry_var)
        user_entry.grid(row=1, column=1, padx=10)

        trial_label = customtkinter.CTkLabel(self.frame_left, text='Trial Number:')
        trial_label.grid(row=2, column=0)
        trial_entry_var = customtkinter.StringVar()
        trial_entry = customtkinter.CTkEntry(self.frame_left, textvariable=trial_entry_var)
        trial_entry.grid(row=2, column=1, padx=10)

        button1 = customtkinter.CTkButton(self.frame_left, text="Submit User/Trial Data", command=self.update_user_data)
        button1.grid(row=3, column=0, columnspan=2, padx=10, pady=20)

        collect_data_box = customtkinter.CTkCheckBox(self.frame_left, text="Record Data", command=self.record_data)
        collect_data_box.grid(row=4, column=0, columnspan=2, padx=50, pady=10)

        run_trial_but = customtkinter.CTkButton(self.frame_left, text="Run Trial", command=self.run_trial)
        run_trial_but.grid(row=5, column=0, columnspan=2, padx=10, pady=20)

        self.frame_left.grid(padx=40, pady=50, row=0, column=0)

        # right frame
        self.frame_right = customtkinter.CTkFrame(master)

        button2 = customtkinter.CTkButton(self.frame_right, text="Update Image to Right", command=self.right_arrow)
        button2.grid(padx=50, pady=20, row=0, column=0)

        button3 = customtkinter.CTkButton(self.frame_right, text="Update Image to Left", command=self.left_arrow)
        button3.grid(padx=50, pady=20, row=1, column=0)

        button3 = customtkinter.CTkButton(self.frame_right, text="Update Image to Stop", command=self.stop_image)
        button3.grid(padx=50, pady=20, row=2, column=0)

        calibrate_but = customtkinter.CTkButton(self.frame_right, text="Calibrate", command=self.calibrate)
        calibrate_but.grid(padx=50, pady=20, row=3, column=0)

        speed_label = customtkinter.CTkLabel(self.frame_right, text='Speed Setting:')
        speed_label.grid(row=4, column=0)
        speed_var = customtkinter.StringVar()
        speed_slider = customtkinter.CTkComboBox(self.frame_right, values=['Slow', 'Medium', 'Fast'], state='normal', command=self.update_speed)
        speed_slider.grid(row=5, column=0, pady=(0,20))

        self.frame_right.grid(padx=20, pady=50, row=0, column=1)

    def open(self):
        self.patientWindow = PatientWindow()

    def update_user_data(self):
        # update csv file with user number and trial num
        # uses .get() with entry text variables
        pass

    def record_data(self):
        # update bool value to update "data collection" function that will take some type of data (eeg,emg)
        pass

    def run_trial(self):
        pass

    def update_speed(self):
        pass

    def right_arrow(self):
        right_img = Image.open("images/right-arrow.gif")
        right_img_resized = right_img.resize((600, 600), Image.Resampling.LANCZOS)
        photo_img = ImageTk.PhotoImage(right_img_resized)
        self.patientWindow.label.config(image=photo_img)
        self.patientWindow.label.image = photo_img

    def left_arrow(self):
        left_img = Image.open("images/left-arrow.gif")
        left_img_resized = left_img.resize((600, 600), Image.Resampling.LANCZOS)
        photo_img = ImageTk.PhotoImage(left_img_resized)
        self.patientWindow.label.config(image=photo_img)
        self.patientWindow.label.image = photo_img

    def stop_image(self):
        # stop_img = Image.open("images/stop.gif")
        # stop_img_resized = stop_img.resize((600, 600), Image.Resampling.LANCZOS)
        # photo_img = ImageTk.PhotoImage(stop_img_resized)
        # self.patientWindow.label.config(image=photo_img)
        # self.patientWindow.label.image = photo_img
        self.patientWindow.stop_image()

    def calibrate(self):
        # send command to motor to go to center
        pass


class PatientWindow():
    def __init__(self):

        top = customtkinter.CTkToplevel()
        top.geometry("600x850")
        top.title("Exoskeleton Patient View")
        self.frame = customtkinter.CTkFrame(top)

        im = Image.open("images/please-wait2.png")
        resized = im.resize((600, 600), Image.Resampling.LANCZOS)
        ph = ImageTk.PhotoImage(resized)

        self.label = Label(self.frame, image=ph, width=600, height=600)
        self.label.image = ph  # need to keep the reference of your image to avoid garbage collection
        self.label.grid(row=0, column=0)
        self.frame.grid(row=0, column=0)

        w = 600
        h = 250

        self.frame_bottom = customtkinter.CTkFrame(top)
        self.canvas = customtkinter.CTkCanvas(self.frame_bottom, width=w, height=h, bg='gray')
        self.canvas.grid(row=0, column=0)

        x = w // 2
        y = h // 2
        cursor = self.canvas.create_oval(x, y, x+10, y+10, fill='red')

        left_wall = self.canvas.create_rectangle(125, 90, 100, 165, fill='pink')

        self.frame_bottom.grid(row=1, column=0)

        # create function that updates canvas here, then call it in main window when needed/condition is met
        # OR have everything in main window like the update image function rn??

    def stop_image(self):
        stop_img = Image.open("images/stop.gif")
        stop_img_resized = stop_img.resize((600, 600), Image.Resampling.LANCZOS)
        photo_img = ImageTk.PhotoImage(stop_img_resized)
        self.label.config(image=photo_img)
        self.label.image = photo_img


    # def canvas_walls(self, position):
    #     self.shape("square")
    #     self.shapesize(stretch_len=1, stretch_wid=5)
    #     self.color("white")
    #     self.penup()
    #     self.goto(position)
    #     self.button1 = Button(self.frame, text="Change", command=self.change_img)
    #     self.button1.pack(padx=20, pady=20)
    #     self.frame.pack()



if __name__ == "__main__":
    root = CTk()
    root.geometry("690x500")
    root.title("Exoskeleton Technician Controls")
    main_window = RootWindow(root)
    root.mainloop()
