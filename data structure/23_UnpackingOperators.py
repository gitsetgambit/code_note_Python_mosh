# well yess we can add number in list just by declaring range
JustAnotherList = list(range(5))

# here '*' is unpacking operator it can unpack strings to
JustAnotherList = [*range(6), *"hello"]
print(JustAnotherList)

# we can unpack two lists also along with string
list1 = [1, 3, 4, 6, 7]
list2 = [2, 6, 5, 3, 5, ]
value = [*list1, *list2, *"aditya"]
print(value)

# same thing with dictionaries
first = {"r": 13}
second = {"x": 30, "y": 45}
combined = {**first, **second, "z": 1}
print(combined)
# but here key value remains
