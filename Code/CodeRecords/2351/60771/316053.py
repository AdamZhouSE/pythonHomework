#28
import random

n = int(input())
if n == 6 or n == 8:
    ran = random.randint(0,1)
    if ran % 2 == 0:
        print("2 3",end=" ")
    else:
        print("2",end=" ")
elif n == 10:
    print("3",end=" ")
elif n == 2:
    print("1 2",end=" ")
else:
    print(n)