def removeElement(nums, val: int) -> int:
    i = 0
    for j in range(len(nums)):
        if nums[j] == val:
            i += 1
            nums.pop(j)
    print(nums)
    return i + 1


print(removeElement([1, 2, 2, 1], 1))
