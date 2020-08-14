file = input('Enter File name or Location to file: ')

if len(file) < 1:
    file = 'textFiles\\clown.txt'

try:
    fileHandler = open(file)
except IOError:
    print('File unable ot open')
    exit()

dictionary = dict()

for line in fileHandler:
    line = line.strip()
    words = line.split()
    for word in words:
        if word not in dictionary:
            dictionary[word] = 1
        else:
            dictionary[word] += 1
print(dictionary)
