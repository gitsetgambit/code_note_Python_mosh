try:
    age = int(input("age:- "))
    xFactor = 10/age
# if age is = 0 then it'll throw an error but
except (ValueError, ZeroDivisionError):
    print("you didn't enter a valid age")
# if same error is thrown amd its declared above
# it will ignore the print statement of the second
# one
except ZeroDivisionError:
    print("you didn't enter a valid age")
else:
    print("no exception were thrown")
