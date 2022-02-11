letters = ["a", "b", "c"]

# index
index = letters.index('b')
print(index)
# add
letters.append("r")
print(letters)
# insert
letters.insert(3, "j")
print(letters)
# remove
letters.pop(2)
print(letters)

# extend
ex = ["f", "t", "u"]
letters.extend(ex)
print("extended list:- ", letters)

# count
count = ex.count("t")
print(count)

# list pop
removed_element = letters.pop(1)
print(removed_element)
print(letters)

# list reverse
rev_list = [2, 4, 6, 7, 8, 9]
rev_list.reverse()
print(rev_list)

# list sort
vowels = ['e', 'a', 'u', 'o', 'i']
vowels.sort()
print('sorted list:- ', vowels)

"""
example 2
"""
vowels.sort(reverse=True)
print('sorted list(in descending):- ', vowels)

# list copy
new_copied_list = letters.copy()
print(new_copied_list)

# list clear
letters.clear()
print(letters)
