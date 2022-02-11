try:
    """
    ('with open("file name") as file) we dont need to
    close the file and we also do not 
    """
    with open("app.py") as file, open("anotherFile.py") as file:
        print("file opened")
    age = int(input("age:- "))
except (ValueError, ZeroDivisionError):
    print("you didn't enter a valid age")
else:
    print("no exception were thrown")
