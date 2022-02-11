try:
    # here we open a file with the 'file=open'
    file = open("3_cleaningUP.py")
    age = int(input("age:- "))
except (ValueError, ZeroDivisionError):
    print("you didn't enter a valid age")
else:
    print("no exception were thrown")
    # here we will use 'finally'method
    # this will execute the 'file.close()'
    # at the end of the program it'll
    # close the file no matter the error or not
finally:
    # 'file.close' is used to close the file
    file.close()
