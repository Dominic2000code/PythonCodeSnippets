def binarySearch(array, firstIndex, lastIndex, x):
    mid = (firstIndex + lastIndex) // 2
    if lastIndex >= firstIndex:
        if array[mid] == x:
            return mid
        elif array[mid] > x:
            return binarySearch(array, firstIndex, mid - 1, x)
        elif array[mid] < x:
            return binarySearch(array, mid + 1, lastIndex, x)
    else:
        return -1


arr = [2, 3, 4, 10, 40]
x_ = 10

# Function call
result = binarySearch(arr, 0, len(arr) - 1, x_)
print(result)
