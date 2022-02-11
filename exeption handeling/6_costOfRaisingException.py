from timeit import timeit

code1 = """
def car_speed(speed):
    if speed <= 0:
        raise ValueError("speed in highway can't be 0 or negetive")
    return 10/speed

try:
    car_speed(5)
except ValueError as error:
    pass
"""

code2 = """
def car_speed(speed):
    if speed <= 0:
        return None
    return 10/speed

speed = car_speed(-5)
if speed == None:
    pass
"""
print("first code time:- ", timeit(code1, number=10000))
print("second code time:- ", timeit(code2, number=10000))

# watch the video again its really deep
