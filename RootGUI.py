from tkinter import *
from PIL import Image, ImageTk


class RootWindow:

    def __init__(self, master):
        self.frame = Frame(master)

        button1 = Button(self.frame, text="Open Patient Window", command=self.open)
        button1.pack(padx=20, pady=20)

        self.frame.pack(padx=10, pady=10)

    def open(self):
        patient_window = PatientWindow()



class PatientWindow:
    def __init__(self):
        top = Toplevel()
        top.geometry("600x600")
        self.frame = Frame(top)

        # self.canvas = Canvas(top, width=600, height=600, bg="black")
        # self.canvas.pack(expand=True)
        # self.images = [PhotoImage(file="images/left-arrow.gif"), PhotoImage(file="images/right-arrow.gif")]
        # self.current_image_number = 0
        # # set first image on canvas
        # self.image_on_canvas = self.canvas.create_image(300, 300, anchor='center', image=self.images[self.current_image_number])
        # self.canvas.itemconfig(self.image_on_canvas, image=self.image_on_canvas)

        im = Image.open("images/left-arrow.gif")
        ph = ImageTk.PhotoImage(im)

        self.label = Label(top, image=ph)
        self.label.image = ph  # need to keep the reference of your image to avoid garbage collection
        self.label.pack()

        self.button1 = Button(self.frame, text="Change", command=self.change_img)
        self.button1.pack(padx=20, pady=20)
        self.frame.pack()

    def change_img(self):
        img2 = ImageTk.PhotoImage(Image.open("images/right-arrow.gif"))
        self.label.configure(image=img2)
        self.label.image = img2


if __name__ == "__main__":
    root = Tk()
    main_window = RootWindow(root)
    root.mainloop()
