from tkinter import *
from tkinter import filedialog

root = Tk()
root.title("Opening Files with dialog box")


def onClick():
    root.filename = filedialog.askopenfilename(
        initialdir=r"C:\Users\Dominic\Desktop\pythoncodes\try\GUI\Image Viewer\images", title="Choose A File",
        filetypes=(
            ("png files", "*.png"), ("jpg files", "*.jpg"), ("All Files", "*.*")))
    mylabel = Label(root, text=root.filename).pack()


myButton = Button(root, text="Choose a file", command=onClick).pack()

root.mainloop()
