numbers = [1, 2, 3, 5, 6, 7, 8]
# here position of variables matter if last is
# writtern before *rest then it'll print the second
# value
first, *rest, last = numbers
"""
here *rest will carry all the elements after [1] [2]
because they are stored in variables before rest
"""
# first = numbers[0]
# second = numbers[0:]
# third = numbers[2]
# print(second)
print(first)
print(last)
print(*rest)
