# checking number is prime or not

x = int(input("enter the num to check:- "))

for n in range(2, x):
    if x % n == 0:
        print("not prime")
        break
else:
    print("num is prime")
