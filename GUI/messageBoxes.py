from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Message Boxes")


# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

def showinfo():
    response = messagebox.showinfo("Info Message", "Download complete")
    Label(root, text="You clicked " + str(response)).pack()


def showwarning():
    response = messagebox.showwarning("Warning Message", "Files may be corrupted")
    Label(root, text="You clicked " + str(response)).pack()


def showerror():
    response = messagebox.showerror("Error Message", "Download failed")
    Label(root, text="You clicked " + str(response)).pack()


def askquestion():
    response = messagebox.askquestion("Buy House", "Do you want to buy house?")
    Label(root, text="You clicked " + str(response)).pack()


def askokcancel():
    response = messagebox.askokcancel("Proceed?", "Do you want to proceed?")
    Label(root, text="You clicked " + str(response)).pack()


def askyesno():
    response = messagebox.askyesno("Continue", "Do you want to continue?")
    Label(root, text="You clicked " + str(response)).pack()


Button(root, text="showinfo", command=showinfo).pack()
Button(root, text="showwarning", command=showwarning).pack()
Button(root, text="showerror", command=showerror).pack()
Button(root, text="askquestion", command=askquestion).pack()
Button(root, text="askokcancel", command=askokcancel).pack()
Button(root, text="askyesno", command=askyesno).pack()

root.mainloop()
