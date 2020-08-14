from tkinter import *

root = Tk()
root.title("Root window")


def onClick():
    secondWindow = Toplevel()
    secondWindow.title("Second window")
    myLabel = Label(secondWindow, text="This is the second window")
    myLabel.pack()
    myButton = Button(secondWindow, text="Back", command=secondWindow.destroy).pack()


mylabel = Label(root, text="This is the main window")
mylabel.pack()
myButton = Button(root, text="Submit", command=onClick).pack()

root.mainloop()
