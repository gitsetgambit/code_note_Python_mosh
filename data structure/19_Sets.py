# here we use 'set' data type in data structure
# to remove all repeting numbers
children = [1, 3, 1, 2, 4, 5, 5]
uniques_only = set(children)
print(uniques_only)

# here we are doing comman tasks with sets we use 'add' instead of append
children_2 = {4, 8}
children_2.add(3)
children_2.remove(3)
print(len(children_2))
print(children_2)

# for adding a whole list to old
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)

# for removing element from set we can also use this
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
