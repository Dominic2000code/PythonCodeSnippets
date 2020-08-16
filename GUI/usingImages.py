from tkinter import *

import requests
from PIL import ImageTk, Image

root = Tk()
# myImg = ImageTk.PhotoImage(Image.open('C:\\Users\\Dominic\\Pictures\\New folder\\a.jpg'))
# myImg = ImageTk.PhotoImage(Image.open('Image Viewer\\images\\a.jpg'))
# mylabel = Label(image=myImg)
# # myImg = ImageTk.PhotoImage(Image.open(r'C:\Users\Dominic\Desktop\MyApps\WeatherApp\icons\wsymbol_0008_clear_sky_night.png.webp'))
# # frame = Label(root, text="Frame", padx=10, pady=10, image=myImg)
# # frame.pack(padx=10, pady=10)
# # frame.grid(row=0, column=0, padx=10, pady=10)
# mylabel.pack()

url = 'https://i.ytimg.com/vi/vEYsdh6uiS4/maxresdefault.jpg'

try:
    resp = requests.get(url, stream=True).raw

except requests.exceptions.RequestException as e:
    sys.exit(1)

# try:
#     img = Image.open(resp)
#
# except IOError:
#     print("Unable to open image")
#     sys.exit(1)
#
# img.save('sid.jpg', 'jpeg')

myImg = ImageTk.PhotoImage(Image.open(resp))
mylabel = Label(image=myImg)
mylabel.pack()

root.mainloop()
