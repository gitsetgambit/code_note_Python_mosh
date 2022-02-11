# speed = int(input("enter the speed:- "))

# if speed >= 100:
#     indication = "Fast"

# elif speed < 20:
#     indication = "Slow"

# else:
#     indication = "Normal"

# print(indication)

speed = int(input("enter the speed:- "))
# can put all conditon in one line elif is not included in this
indication = "Fast" if speed >= 100 else "normal"
# just simply print the indication
print(indication)
