def search(nums, key):
    for i in range(len(nums)):
        if nums[i] == key:
            return i
        # elif key not in nums:
        #     return -1
    return -1


index = search([8, 6, 10, 50, 1, 2, 19], 10)
print(index)
