from array import array

number = array("i", [1, 2, 4])
number[0] = 4.0
print(number)
# this will give Error
# because array takes only solid integer values
# and they are only used when there is a performance issue
# they are generally faster then the list but rarely used
