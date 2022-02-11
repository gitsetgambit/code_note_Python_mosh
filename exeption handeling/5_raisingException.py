def car_speed(speed):
    # here
    if speed <= 0:
        raise ValueError("speed in highway can't be 0 or negetive")
    return 10/speed


# here we normal exception handeling
try:
    car_speed(int(input("enter the car speed:- ")))
except ValueError as error:
    print(error)
