"""
Given an integer array sorted in non-decreasing order, return an array of the squares of each number sorted in
non-decreasing order.
"""


def sortedSquares(nums):
    n = len(nums)
    start, end = 0, n - 1
    result = [0] * n
    index = n - 1

    while end > -1 and index > -1:
        if abs(nums[start]) > abs(nums[end]):
            result[index] = nums[start] ** 2
            start += 1
        else:
            result[index] = nums[end] ** 2
            end -= 1
        index -= 1

    return result


print(sortedSquares([-4, -3, -2, 0, 1, 2, 5, 10]))
