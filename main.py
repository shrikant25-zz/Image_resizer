import PIL.Image
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import messagebox as mb
import os


class MainWindow:
    def __init__(self, win):
        self.filename = None
        self.uploaded_image = None
        self.reduced_image = None
        self.heading = Label(win, text="Image Size Modifier", fg="red",
                             font=("Helvetica", 36))  # set the heading using Label class with its attributes
        self.heading.place(x=300, y=50)  # heading coordinates coordinates
        self.insert_image_btn = Button(win, text="Insert Image", bg="skyblue", fg="red",
                                       bd=7,
                                       command=self.insert)  # setting button with Button class, when click calls the insert function
        self.insert_image_btn.place(x=380, y=150)  # button coordinates
        self.height_label = Label(win, text="Height")  # just a label
        self.height_label.place(x=300, y=220)  # placing the label
        self.height_box = Entry(win, bd=4)  # box takes values for height from user
        self.height_box.place(x=350, y=220)  # placing the box
        self.width_label = Label(win, text="Width")  # just a label
        self.width_label.place(x=300, y=250)  # placing the label
        self.width_box = Entry(win, bd=4)  # box takes values for width from user
        self.width_box.place(x=350, y=250)  # placing th box
        self.Resize_image_btn = Button(win, text="Resize Image", bg="skyblue", fg="red",
                                       bd=7,
                                       command=self.resize)  # setting button with Button class, when clicked it calls the resize function
        self.Resize_image_btn.place(x=380, y=300)  # button coordinates

    def insert(self):
        try:
            self.filename = askopenfilename()  # prompts user to select/name a file
            self.uploaded_image = PIL.Image.open(self.filename)  # opens the file ans sets the path in class variable
        except:
            mb.showerror("Error", "Cannot open the file")  # if failed error is shown

    def resize(self):
        if not self.height_box.get() or not self.width_box.get():  # checks if values are present in the variables
            mb.showerror("Error", "Height and Width must be specified")  # if not then error is shown
            self.width_box.delete(0, 'end')  # clears the input box for width
            self.height_box.delete(0, 'end')  # clears the input box fro height
        else:
            try:
                height = int(self.height_box.get())  # converts the input into integer
                width = int(self.width_box.get())  # converts the input into integer
                newsize = (width, height)  # sets the width and height values to a variable
                self.reduced_image = self.uploaded_image.resize(
                    newsize)  # resizes the image and sets the image paht to class variable
                self.save()  # calls the save function
            except:
                self.width_box.delete(0, 'end')  # clears the values in input box
                self.height_box.delete(0, 'end')  # clears the values in input box
                mb.showerror("Error", "Failed to resize")  # raises an error if resizing fails

    def save(self):
        file_name = os.path.basename(self.filename)  # extracts the file name from path
        self.reduced_image = self.reduced_image.save(str(file_name))  # saves the file
        try:
            saved_file_path = os.path.join(os.getcwd(), file_name)
            '''joins he current directories path and file name
               and stores the the path in a variable
               the variable can be used to show a message that
               informs the user about the path where the file is saved
            '''
            mb.showinfo("saved", f"File saved at {saved_file_path}")
            self.width_box.delete(0, 'end')  # clears the input box
            self.height_box.delete(0, 'end')  # clears the input box
        except:
            mb.showerror("Error", "Failed to save the file")  # shows an error if fails to save the file


window = Tk()  # creates a top-level window having frame, title bar, control-block with minimize and close buttons
main_window = MainWindow(window)  # creates an instance of the class
window.title('Image Resizer')  # set title
window.geometry("900x600+250+100")  # set width, height, x-cord and y-cord
window.mainloop()  # enters in an event listening loop
