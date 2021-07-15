def reverseArray(arr):
    start, end = 0, len(arr) - 1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


a = [10, 20, 30, 40, 50]
reverseArray(a)
print(a)
