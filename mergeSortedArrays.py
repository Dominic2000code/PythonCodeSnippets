array1 = [0, 3, 4, 31]
array2 = [4, 6, 30]


def mergeSortedArrays(arr1, arr2):
    mergedArray = []
    if len(arr1) == 0:
        return arr2
    if len(arr2) == 0:
        return arr1

    while len(arr1) != 0 and len(arr2) != 0:
        arr1Item = arr1[0]
        arr2Item = arr2[0]
        if arr1Item <= arr2Item:
            mergedArray.append(arr1Item)
            arr1.remove(arr1Item)
        else:
            mergedArray.append(arr2Item)
            arr2.remove(arr2Item)

    while len(arr1) != 0:
        mergedArray.append(arr1.pop())
    while len(arr2) != 0:
        mergedArray.append(arr2.pop())

    return mergedArray


print(mergeSortedArrays(array1, array2))
