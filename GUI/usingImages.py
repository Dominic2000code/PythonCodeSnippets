from tkinter import *
from PIL import ImageTk, Image

root = Tk()
# myImg = ImageTk.PhotoImage(Image.open('C:\\Users\\Dominic\\Pictures\\New folder\\a.jpg'))
myImg = ImageTk.PhotoImage(Image.open('Image Viewer\\images\\a.jpg'))
mylabel = Label(image=myImg)
mylabel.pack()
root.mainloop()
