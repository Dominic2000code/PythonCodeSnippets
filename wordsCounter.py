file = input('Enter File name: ')

if len(file) < 1:
    file = r'textFiles\\clown.txt'
try:
    fileHandler = open(file)
except IOError:
    print("File unable to open file")
    exit()

wordCount = 0

for line in fileHandler:
    # print(line)
    li = line.split()
    # print(li)
    for word in li:
        wordCount += 1

print(wordCount)
