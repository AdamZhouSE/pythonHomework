import math
n = int(input())
if n == 0:
    print("False")
else:
    a = str(math.log(n, 3)).split(".")
    if a[1] == '0':
        print("True")
    else:
        print("False")