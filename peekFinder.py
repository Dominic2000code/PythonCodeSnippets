"""
 Peek finder
 One-dimensional version
 Given an array of integers arr = [a,b,c,d,e,f,g,h,i] a-i are numbers
 Position 2 is a peek if and only if b>= a and b>=c
 Position 1 is a peek if a>=b and Position 9 is a peek if i>=h
"""


# Time complexity for this approach is O(n). Linear time
def peekFinder(nums):
    if len(nums) == 0:
        return 0
    elif len(nums) == 1:
        return nums[0]
    elif nums[0] >= nums[1]:
        return nums[0]
    elif nums[len(nums) - 1] >= nums[len(nums) - 2]:
        return nums[len(nums) - 1]
    for i in range(len(nums)):
        if nums[i + 1] >= nums[i] and nums[i + 1] >= nums[i + 2]:
            return nums[i + 1]


# Time complexity for this approach is O(log(n)). Logarithmic time
def efficientPeekFinder(nums, firstIndex, lastIndex):
    mid = (firstIndex + lastIndex) // 2
    if nums[mid] >= nums[mid - 1] and nums[mid] >= nums[mid + 1]:
        return nums[mid]
    elif nums[mid] < nums[mid - 1]:
        return efficientPeekFinder(nums, firstIndex, lastIndex)
    elif nums[mid] < nums[mid + 1]:
        return efficientPeekFinder(nums, mid, lastIndex)


nums_ = [1, 3, 4, 20, 1, 0, 5]
peek = efficientPeekFinder(nums_, 0, len(nums_) - 1)
print("Peek element:", peek)
