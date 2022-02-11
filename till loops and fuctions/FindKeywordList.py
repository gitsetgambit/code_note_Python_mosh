import keyword
from typing import Counter

kw = keyword.kwlist
print(kw)

# 1st method to find total number of keyword
num = len(kw)
print(num)

# 2nd method to find total number of keyword


def get_the_number(kw):
    Count = 0
    for i in kw:
        Count += 1
    print(Count)


get_the_number(kw)
