import math
num = int(input())

def judge(num):
    a = 0
    b = int(math.sqrt(num))
    while (a <= b):
        add = a * a + b * b
        if add == num:
            return True
        elif add > num:
            b = b - 1
        else:
            a = a + 1
    return False

print(judge(num))