"""
       *
      **
     ***
    ****
     ***
      **
       *
"""
n = 4
for i in range(n, 0, -1):
    print(i*" ", end="")
    print((n-i)*"*")
for r in range(0, n):
    print(r*" ", end="")
    print((n-r)*"*")
