from tkinter import *
from PIL import Image, ImageTk
from ArduinoPython import ArduinoCode


class RootWindow:

    def __init__(self, master):
        self.frame = Frame(master)
        self.patientWindow = None

        button1 = Button(self.frame, text="Open Patient Window", command=self.open)
        button1.pack(padx=20, pady=20)

        button2 = Button(self.frame, text="Update Image to Right", command=self.right_arrow)
        button2.pack(padx=50, pady=20)

        button3 = Button(self.frame, text="Update Image to Left", command=self.left_arrow)
        button3.pack(padx=50, pady=20)

        button3 = Button(self.frame, text="Update Image to Stop", command=self.stop_image)
        button3.pack(padx=50, pady=20)

        self.frame.pack(padx=50, pady=20)

    def open(self):
        self.patientWindow = PatientWindow()

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
        stop_img = Image.open("images/stop.gif")
        stop_img_resized = stop_img.resize((600, 600), Image.Resampling.LANCZOS)
        photo_img = ImageTk.PhotoImage(stop_img_resized)
        self.patientWindow.label.config(image=photo_img)
        self.patientWindow.label.image = photo_img


class PatientWindow:
    def __init__(self):
        top = Toplevel()
        top.geometry("600x600")
        self.frame = Frame(top)

        im = Image.open("images/please-wait2.png")
        resized = im.resize((600, 600), Image.Resampling.LANCZOS)
        ph = ImageTk.PhotoImage(resized)

        self.label = Label(top, image=ph, width=600, height=600)
        self.label.image = ph  # need to keep the reference of your image to avoid garbage collection
        self.label.pack()

    #     self.button1 = Button(self.frame, text="Change", command=self.change_img)
    #     self.button1.pack(padx=20, pady=20)
    #     self.frame.pack()
    #
    # def change_img(self):
    #     img2 = ImageTk.PhotoImage(Image.open("images/right-arrow.gif"))
    #     self.label.configure(image=img2)
    #     self.label.image = img2


if __name__ == "__main__":
    root = Tk()
    main_window = RootWindow(root)
    root.mainloop()
