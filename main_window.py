import csv
import time
from tkinter import *
from PIL import Image, ImageTk
import customtkinter
from customtkinter import *
import turtle
from window_creation import PlanarWindowCreation, GloveWindowCreation, ActiveControlGUI

customtkinter.set_appearance_mode("system")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green
LEFT = (-450, 0)
RIGHT = (450, 0)
CLOSE_LEFT = (-225, 0)
CLOSE_RIGHT = (225, 0)
now = time.ctime()
print("Current Time:", now)


# open passive control: its controls underneath it
# open active (push button) control -- add planar control together, if active then the arduino will do work and python will just print it
# open glove GUI/ controls under it
# open both glove and active control GUI??
# if specific GUI open then buttons/controls/functions able to work


class RootWindow:

    def __init__(self, master):
        # self.patientWindow = PatientWindow()  # opens patient window
        # self.arduino_data = PythonArduino()  # pull in arduino data object
        self.sub_window = None
        self.sub_window2 = None
        self.sub_window3 = None
        self.position = None  # used as variable for position data from received Arduino position data
        # left frame
        self.frame_1 = customtkinter.CTkFrame(master)

        user_label = customtkinter.CTkLabel(self.frame_1, text='User Number:')
        user_label.grid(row=1, column=0, pady=20)
        self.user_entry_var = customtkinter.StringVar()
        user_entry = customtkinter.CTkEntry(self.frame_1, textvariable=self.user_entry_var)
        user_entry.grid(row=1, column=1, padx=10)

        trial_label = customtkinter.CTkLabel(self.frame_1, text='Trial Number:')
        trial_label.grid(row=2, column=0)
        self.trial_entry_var = customtkinter.StringVar()
        trial_entry = customtkinter.CTkEntry(self.frame_1, textvariable=self.trial_entry_var)
        trial_entry.grid(row=2, column=1, padx=10)

        submit_button = customtkinter.CTkButton(self.frame_1, text="Submit User/Trial Data",
                                                command=self.update_user_data)
        submit_button.grid(row=3, column=0, columnspan=2, padx=10, pady=20)

        collect_data_box = customtkinter.CTkCheckBox(self.frame_1, text="Record Data", command=self.record_data)
        collect_data_box.grid(row=4, column=0, columnspan=2, padx=50, pady=10)

        speed_label = customtkinter.CTkLabel(self.frame_1, text='Speed Setting:')
        speed_label.grid(row=5, column=0, columnspan=2, pady=(20, 0))
        self.speed_var = customtkinter.StringVar()
        speed_slider = customtkinter.CTkComboBox(self.frame_1, variable=self.speed_var, values=['Slow', 'Fast'],
                                                 state='normal', command=self.update_speed)
        speed_slider.grid(row=6, column=0, columnspan=2, padx=10, pady=20)

        self.open_active_but = customtkinter.CTkButton(self.frame_1, text="Active Control Window",
                                                       command=self.open_active_window,
                                                       fg_color="green")
        self.open_active_but.grid(row=8, column=0, columnspan=2, padx=10, pady=20)

        self.enable_tech_but = customtkinter.CTkButton(self.frame_1, text="Enable Tech Mode",
                                                       command=lambda: [self.enable_tech_mode(), self.enable_buttons()],
                                                       fg_color="green")
        self.enable_tech_but.grid(row=7, column=0, columnspan=2, padx=10, pady=20)

        self.frame_1.grid(padx=40, pady=50, row=0, column=0)

        # second frame

        self.frame_2 = customtkinter.CTkFrame(master)

        self.open_exo_but = customtkinter.CTkButton(self.frame_2, text="Open Planar Window",
                                                    command=self.open_planar_exo_window)
        self.open_exo_but.grid(row=0, column=0, columnspan=1, padx=10, pady=20)

        self.close_exo_but = customtkinter.CTkButton(self.frame_2, text="Close Planar Window",
                                                     command=self.close_planar_exo_window)
        self.close_exo_but.grid(row=0, column=1, columnspan=1, padx=10, pady=20)

        self.close_left_but = customtkinter.CTkButton(self.frame_2, text="Go Close Left",
                                                      command=self.go_close_left)
        self.close_left_but.grid(padx=50, pady=20, row=1, column=0)

        self.far_left_but = customtkinter.CTkButton(self.frame_2, text="Go Far Left",
                                                    command=self.go_far_left)
        self.far_left_but.grid(padx=50, pady=20, row=2, column=0)

        self.close_right_but = customtkinter.CTkButton(self.frame_2, text="Go Close Right",
                                                       command=self.go_close_right)
        self.close_right_but.grid(padx=50, pady=20, row=1, column=1)

        self.far_right_but = customtkinter.CTkButton(self.frame_2, text="Go Far Right",
                                                     command=self.go_far_right)
        self.far_right_but.grid(padx=50, pady=20, row=2, column=1)

        self.center_but = customtkinter.CTkButton(self.frame_2, text="Go to Center",
                                                  command=self.go_to_center)
        self.center_but.grid(padx=50, pady=20, row=4, column=0, columnspan=2)

        self.calibrate_but = customtkinter.CTkButton(self.frame_2, text="Calibrate",
                                                     command=self.calibrate)
        self.calibrate_but.grid(padx=50, pady=20, row=5, column=0, columnspan=2)

        self.run_trial_but = customtkinter.CTkButton(self.frame_2, text="Run Trial",
                                                     command=self.run_trial,
                                                     fg_color="green")
        self.run_trial_but.grid(row=6, column=0, columnspan=1, padx=10, pady=20)

        self.stop_but = customtkinter.CTkButton(self.frame_2, text="Stop Trial",
                                                command=self.stop_trial, fg_color="red")
        self.stop_but.grid(padx=50, pady=20, row=6, column=1, columnspan=1)

        self.frame_2.grid(padx=20, pady=50, row=0, column=1)

        # Third Frame

        self.frame_3 = customtkinter.CTkFrame(master)

        self.open_glove_but = customtkinter.CTkButton(self.frame_3, text="Open Glove Window",
                                                      command=self.open_glove_window)
        self.open_glove_but.grid(row=0, column=0, columnspan=1, padx=10, pady=10)

        self.close_glove_but = customtkinter.CTkButton(self.frame_3, text="Close Glove Window",
                                                       command=self.close_glove_window)
        self.close_glove_but.grid(row=0, column=1, columnspan=1, padx=10, pady=10)

        self.open_hand_but = customtkinter.CTkButton(self.frame_3, text="Open Hand",
                                                     command=self.open_glove)
        self.open_hand_but.grid(row=1, column=0, columnspan=1, padx=10, pady=10)

        self.close_hand_but = customtkinter.CTkButton(self.frame_3, text="Close Hand",
                                                      command=self.close_glove)
        self.close_hand_but.grid(row=1, column=1, columnspan=1, padx=10, pady=10)

        self.run_glove_trial = customtkinter.CTkButton(self.frame_3, text="Run Trial",
                                                       command=self.run_glove_trial,
                                                       fg_color="green")
        self.run_glove_trial.grid(row=2, column=0, columnspan=1, padx=10, pady=10)

        self.stop_glove = customtkinter.CTkButton(self.frame_3, text="Stop Trial",
                                                  command=self.stop_glove_trial,
                                                  fg_color="red")
        self.stop_glove.grid(padx=10, pady=10, row=2, column=1, columnspan=1)

        self.frame_3.grid(padx=20, pady=50, row=0, column=2)

    # Root Window Functions (Glove, Planar)

    # Data recording/Enable tech functions

    def enable_tech_mode(self):
        # self.arduino_data.send_data("Tech Mode arduino string here**")
        print("Tech mode enabled")

    def enable_buttons(self):
        self.open_exo_but['state'] = NORMAL
        self.close_exo_but["state"] = NORMAL
        self.close_left_but["state"] = NORMAL
        self.far_left_but["state"] = NORMAL
        self.close_right_but["state"] = NORMAL
        self.far_right_but["state"] = NORMAL
        self.center_but["state"] = NORMAL
        self.calibrate_but["state"] = NORMAL
        self.run_trial_but["state"] = NORMAL
        self.stop_but["state"] = NORMAL
        self.open_glove_but["state"] = NORMAL
        self.close_glove_but["state"] = NORMAL
        self.open_hand_but["state"] = NORMAL
        self.close_hand_but["state"] = NORMAL
        self.run_glove_trial["state"] = NORMAL
        self.stop_glove["state"] = NORMAL

    def open_active_window(self):
        self.sub_window3 = ActiveControlGUI()
        print("Active Control Window Open")

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
        # update bool value to update "data collection" function that will take some type of data
        pass

    # Glove Functions
    def open_planar_exo_window(self):
        self.sub_window = PlanarWindowCreation()
        print("Planar Window Created")

    def close_planar_exo_window(self):
        self.sub_window.close_window()
        print("Planar Window Closed")

    def open_glove_window(self):
        self.sub_window2 = GloveWindowCreation()
        print("Glove Window Created")

    def close_glove_window(self):
        self.sub_window2.close_window()  # need the whole window to load and print out "created" statement before closing
        print("Glove Window Closed")

    def open_glove(self):
        self.sub_window2.open_hand_image()

    def close_glove(self):
        self.sub_window2.close_hand_image()

    def run_glove_trial(self):
        self.sub_window2.open_hand_image()

        self.sub_window2.close_hand_image()

        self.sub_window2.open_hand_image()

        self.sub_window2.close_hand_image()

        self.sub_window2.open_hand_image()

        self.sub_window2.good_job_img()

    def stop_glove_trial(self):
        pass

    # Planar system functions

    def run_trial(self):
        pass

    def stop_trial(self):
        pass

    def update_speed(self, speed):
        pass

    def set_heading(self, direction):
        pass

    def go_to_center(self):
        pass

    def go_close_left(self):
        pass

    def go_close_right(self):
        pass

    def go_far_left(self):
        pass

    def go_far_right(self):
        pass

    def calibrate(self):
        pass


if __name__ == "__main__":
    root = CTk()
    root.geometry("%dx%d+%d+%d" % (1280, 540, 300, 300))
    root.title("Exoskeleton Technician Controls")
    main_window = RootWindow(root)
    root.mainloop()
