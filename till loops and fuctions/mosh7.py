# taking the integer could be float that can take decimal values as well
temperature = float(input("temp: - "))
if temperature > 45:
    print("its hot out there")
    print("you'll get burned")

# another condition we use elif inside the if for another condition
elif temperature < 20:
    print("its cold")
    print("you'll get sick")

# or else print this
else:
    print("its noraml")

# this is out of the indentation of the loop so it'll print no matter
# condition of the loop it'll always print
print("only go out when its normal")
