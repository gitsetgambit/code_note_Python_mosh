# we can define dictionaries in these ways
dictionary = {"x": 7, "y": 45}
dictionary = dict(x=7, y=45)

# we can assign/change the values
dictionary["x"] = 34
# we can also add new element just by adding the valuie with it
dictionary["z"] = 31
print(dictionary)

# if something is not present it'll show error of if its
# present it'll just print it
if "a" in dictionary:
    print(["a"])

# another way is with 'get' method if its not present
# just print '0'
print(dictionary.get("a", 0))

# 'del' is for deleting the element
del dictionary["x"]
print(dictionary)

"""
here we will try to print the dictionary in various ways
"""
# just key values will be printed
for x in dictionary:
    print(x)

# it will print both key and value
for x in dictionary:
    print(x, dictionary[x])

# be printed in the form of tuple
for x in dictionary.items():
    print(x)

# it will also print both with 'item' method
for key, value in dictionary.items():
    print(key, value)

# 'get' used case
"""
from w3 school 'get' use case

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(
car.get("model")
)
"""

# 'change' the value
"""
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["year"] = 2020
"""
# 'adding' new key value
"""
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"]="red"
"""
# 'pop'
"""
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")
"""
# clear
"""
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()
"""
