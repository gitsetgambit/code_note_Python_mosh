"""
       *
      * *
     *   *
    *     *
   *       *
  *         *
 * * * * * * *
"""

n = 6
for i in range(1, 6):
    if i == 1:
        print((7)*" " + "*")
    print((n-i)*" ", end="")
    print("*" + (i)*"  " + "*")
for s in range(7):
    print("* ", end="")
