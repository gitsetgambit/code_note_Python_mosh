# this is also a tupple
point = 1,
print(type(point))

# this will be considered as a "int"
point = 1
print(type(point))

# concatination of a tupple
point = (1, 2)+(3, 4)
print(point)

# multiplication of two tupple
point = (1, 5) * 2
print(point)

# convert any iterable to tupple
point = tuple("aditya")
print(point)

# printing elemnets from the index
point = (1, 3, 6, 7)
print(point[0:2])

"""
tupples are immutable
"""
