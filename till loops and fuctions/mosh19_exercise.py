# print all the even numbers and count the total number of even numbers

count_even = 0
for numbers in range(1, 14):
    if numbers % 2 == 0:
        print(numbers, " ", end="")
        count_even += 1
print("\nnumber evens we have", count_even)
