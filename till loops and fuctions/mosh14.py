successful = True
for number in range(3):
    print("Attempt")
    if successful:
        print("successful")
        break
else:
    print("tried 3 times and failed")
