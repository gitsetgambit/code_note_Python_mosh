def medicine(patients, doses):
    for i in patients:
        for r in doses:
            print(f"({i} -> {r})")


patients = ["aditya", "aman", "mainu"]
doses = ["dose1", "dose2", "dose3"]
# print(medicine)
medicine(patients, doses)
