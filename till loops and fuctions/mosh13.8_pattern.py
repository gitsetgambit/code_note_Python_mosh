"""  
* * * * * 
 * * * *
  * * *
   * *
    *
    *
   * *
  * * *
 * * * *
"""
n = 5
for i in range(1, 6):
    print((i-1)*" ", end="")
    print((n-i+1)*"* ")
    # print(i)
for r in range(1, 6):
    print((n-r)*" ", end="")
    print((r)*"* ")
