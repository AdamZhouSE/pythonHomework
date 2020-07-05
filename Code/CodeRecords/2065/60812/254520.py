import math
try:
    a = int(input().strip(' '))
    if a <= -math.pow(2, 31):
        print(int(-math.pow(2, 31)))
    elif a > math.pow(2, 31)-1:
        print(int(math.pow(2, 31)-1))
    else:
        print(a)
except ValueError:
    print(0)