data = [[1, 5], [2, 18], [3, 21]]

pos, value = 0, 0

for i in range(len(data)):
    if data[i][1] > value:
        value = data[i][1]
        pos = data[i][0]
    print(data[i][1])
print("the greatest value is: ", value, " and the position is: ", pos)
