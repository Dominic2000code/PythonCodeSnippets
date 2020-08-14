smallestSoFar = None

for the_num in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    if smallestSoFar is None:
        smallestSoFar = the_num
    elif the_num < smallestSoFar:
        smallestSoFar = the_num
print("Smallest Number is: ", smallestSoFar)
