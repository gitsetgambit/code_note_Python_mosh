def multiply(*numbers):
    # when we write *before a singular argument
    # then we can take as many numbers inside
    total = 1
    for number in numbers:
        # (total = total * number) instead
        # we can write this
        total *= number
    return total


print(multiply(2, 3, 7, 9))
