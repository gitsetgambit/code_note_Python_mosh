# declaring set 'with' method keyword set is long
children = [7, 1, 3, 1, 2, 4, 5, 5]
first_set = set(children)

# its a better way to declare set
second_set = {5, 8}

# doing methmatical tasks using set operators

# union of two sets
print(first_set | second_set)
# intersection
print(first_set & second_set)
# diffrence
print(first_set - second_set)
# symmetric diffrence
print(first_set ^ second_set)

# if 1 is in first_set it'll print "yess"
if 7 in first_set:
    print("yess")
