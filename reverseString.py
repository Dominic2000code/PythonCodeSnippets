dummyString = "Hi My name is Dominic"


# Method 1 Time Complexity O(n) Space Complexity O(n)
# def revereString(string):
# container = []
#     newString = ""
#     for i in string:
#         container.append(i)
#
#     for item in range(len(container)):
#         newString += container.pop()
#     return newString

# Method 2 Time Complexity O(n) Space Complexity O(1)
def revereString2(string):
    newString = ""
    for i in range(len(string) - 1, -1, -1):
        newString += string[i]
    return newString


print(dummyString)
# print(revereString(dummyString))
print(revereString2(dummyString))
