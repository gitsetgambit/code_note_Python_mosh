x = input("enter the number or string to check :- ")

y = (x[::-1])

print("palindrome") if x == y else print("not palindrome")
