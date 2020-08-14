from tkinter import *

root = Tk()
root.title("Frames")

frame = LabelFrame(root, text="Frame", padx=50, pady=50)
frame.pack(padx=10, pady=10)

myButton = Button(frame, text="Button 1 ")
# myButton.pack() #or
myButton.grid(row=0, column=0)

myButton2 = Button(frame, text="Button 2 ")
myButton2.grid(row=1, column=1)

root.mainloop()
