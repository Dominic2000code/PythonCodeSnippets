def removeDuplicates(nums) -> int:
    i = 0
    for j in range(len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]

    return i + 1


print(removeDuplicates([1, 1, 2]))
