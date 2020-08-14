from tkinter import *

root = Tk()


def onClick():
    myLabel = Label(root, text="Clicked")
    myLabel.pack()


myButton = Button(root, text="Click moi", fg="black", bg="white", command=onClick)
myButton.pack()
root.mainloop()
