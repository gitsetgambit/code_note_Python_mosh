# we will import 'sys' module to use 'getsizeof'
from sys import getsizeof

# here we are using the normal comprehensive one line loop
# but here 'getsizeof' is bringing the size of memory
# this range(100000) using
# here we used generator expression
values = (x*2 for x in range(100000))
print("gen:", getsizeof(values))

# here used normal list
# same thing with list
values = [x*2 for x in range(100000)]
print("List:", getsizeof(values))

"""
actually using '()' will use less memory then '[]'
this will save memory and handle big stream of data
"""
