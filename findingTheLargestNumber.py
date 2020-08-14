largestNumberSoFar = None

for value in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    if largestNumberSoFar is None:
        largestNumberSoFar = value
    elif value > largestNumberSoFar:
        largestNumberSoFar = value
print("The largest number is: ", largestNumberSoFar)
