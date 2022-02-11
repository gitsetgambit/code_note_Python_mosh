def fizz_buzz(number):
    if number % 5 == 0 and number % 3 == 0:
        return "FizzBuzz"
    elif number % 5 == 0:
        return "Fizz"
    elif number % 3 == 0:
        return "Buzz"
    return number


x = int(input("enter the number:- "))
print(fizz_buzz(x))
