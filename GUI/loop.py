import re

fileName = "images.txt"
fhandler = open(fileName)

img = list()

for line in fhandler:
    # line = line.lstrip
    img.append(line)
    # print(img)

newImg = list()
for i in img:
    i = i.strip()
    newImg.append(i)
    print(i)
print(newImg)



