try:
    age = int(input("age: "))
except ValueError:
    print("name cannot be a number")
else:
    print("no exception were thrown")
print("execution continues")
