from tkinter import *
from PIL import ImageTk, Image

fileName = "images.txt"  # name of file containing location of images
fhandler = open(fileName)  # file handler that opens the file

img = list()  # list that contains the location of images in memory with whitespace

# a for loop that loops through the fhandler and appends it to the img list
for line in fhandler:
    img.append(line)

newImg = list()  # this list contains the location of the images in memory but without whitespace
# a for loop that loops through the img list and removes any whitespace
for i in img:
    i = i.strip()
    newImg.append(i)

root = Tk()
root.title("Image Viewer")

image_list = []  # final image list the contains the images with pillow config
for image in newImg:
    image_list.append(ImageTk.PhotoImage(Image.open(image)))  # adding pillow config and appending to the image_list

statusNum = Label(root, text="Image 1 of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
# bd is border relief is the depth and anchor is the position

mylabel = Label(image=image_list[0])
mylabel.grid(row=0, column=0, columnspan=3)


def forward(image_number):
    global mylabel
    global button_forward
    global button_back

    mylabel.grid_forget()
    mylabel = Label(image=image_list[image_number - 1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))
    button_back = Button(root, text="<<", command=lambda: backward(image_number - 1))
    mylabel.grid(row=0, column=0, columnspan=3)

    if image_number == len(image_list):
        button_forward = Button(root, text=">>", state=DISABLED)

    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
    statusNum = Label(root, text="Image " + str(image_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN,
                      anchor=E)
    statusNum.grid(row=2, column=0, columnspan=3, sticky=W + E)


def backward(image_number):
    global mylabel
    global button_forward
    global button_back

    mylabel.grid_forget()
    mylabel = Label(image=image_list[image_number - 1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))
    button_back = Button(root, text="<<", command=lambda: backward(image_number - 1))
    mylabel.grid(row=0, column=0, columnspan=3)

    if image_number == 1:
        button_back = Button(root, text="<<", state=DISABLED)

    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
    statusNum = Label(root, text="Image " + str(image_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN,
                      anchor=E)
    statusNum.grid(row=2, column=0, columnspan=3, sticky=W + E)


button_back = Button(root, text="<<", command=backward, state=DISABLED)
button_exit = Button(root, text="Exit Viewer", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(2))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2, pady=15)
statusNum.grid(row=2, column=0, columnspan=3, sticky=W + E)
# sticky is for positioning the label statically so a position

root.mainloop()
