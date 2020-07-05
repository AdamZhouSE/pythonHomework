import math
n = int(input())
a = str(math.log(n, 2)).split(".")
if a[1] == '0':
    print("True")
else:
    print("False")