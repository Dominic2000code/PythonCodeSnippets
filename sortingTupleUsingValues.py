dictionary = {'a': 1, 'd': 2, "c": 3, 'b': 25}
li = list()
for k, v in dictionary.items():
    li.append((v, k))
li = sorted(li, reverse=True)
print(li)


# Shorter Approach
NewLi = sorted([(v, k) for k, v in dictionary.items()], reverse=True)
print(NewLi)
