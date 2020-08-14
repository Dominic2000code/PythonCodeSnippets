import re

fhandler = open("textFiles//regxExample.txt")

for line in fhandler:
    if re.search('^console', line):
        print(line)
