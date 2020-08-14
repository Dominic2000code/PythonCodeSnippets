from tkinter import *

root = Tk()
fname = Entry(root, width=20)
fnameLabel = Label(root, text="First name")
lname = Entry(root, width=20)
lnameLabel = Label(root, text="Last name")

fnameLabel.grid(row=0, column=0)
fname.grid(row=0, column=1)
lnameLabel.grid(row=0, column=3)
lname.grid(row=0, column=4)


def onclick():
    greetings = "Hello " + fname.get() + " " + lname.get()
    mylabel = Label(root, text=greetings)
    mylabel.grid(row=3, column=3)


myButton = Button(root, text="Submit", command=onclick)
myButton.grid(row=2, column=3)

root.mainloop()
