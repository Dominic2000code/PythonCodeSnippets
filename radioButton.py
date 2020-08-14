from tkinter import *

root = Tk()
root.title("Radio Buttons")

Schools = [
    ("GIMPA", "GIMPA"),
    ("Legon", "Legon"),
    ("UPSA", "UPSA"),
    ("KNUST", "KNUST")
]

schVar = StringVar()
schVar.set("GIMPA")


def onclick(value):
    mylabel = Label(root, text=value)
    mylabel.pack(anchor=W)


for text, school in Schools:
    Radiobutton(root, text=text, variable=schVar, value=school, command=lambda: onclick(schVar.get())).pack(anchor=W)

# myButton = Button(root, text="Choose", command=lambda: onclick(schVar.get()))
# myButton.pack()
myLabel = Label(root, text=schVar.get(), pady=10).pack(anchor=W)

root.mainloop()
