# this one is the global variable as it is outside
# and before the indentation of of function def
shopping_complex = "city based"


def market(name):
    # global shopping_complex (this is bad practice)
    # when we make a local variable global it may affect
    # other variables with same name
    shopping_complex = "areas based"


market("market 1")
print(shopping_complex)
# it is printing the global variable which is outside
# the def func.
