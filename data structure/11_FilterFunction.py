items = [
    ("product1", 10),
    ("product2", 9),
    ("product3", 12),
    ("product4", 17),
    ("product5", 3),
    ("product6", 40),

]
filtered = list(filter(lambda i: i[1] >= 10, items))
print(filtered)

"""
# we are changing output in a 'list'
# 'filter' is a method we used here to take a function which is 'lambda'
   here. 
# 'i:i[1]' is parameter inside lambda which is iterating second value of 
    the tupple because'[1]' 
# 'i:i[1]>=10 is parameter we want to check and filter
#  'items' is the list we are working in 
# finally we are printing the variable we stored the list in 
    'filtered'
"""
