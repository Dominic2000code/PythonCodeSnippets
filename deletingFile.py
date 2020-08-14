import os

# os.remove("text.txt")
# print("File deleted")


for file in os.listdir("C:\\Users\\Dominic\\Desktop\\pythoncodes\\try\\textFiles"):
    os.remove("C:\\Users\\Dominic\\Desktop\\pythoncodes\\try\\textFiles\\"+file)
    print(file, "deleted")
