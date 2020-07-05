import math

def solve():
    num = int(input())
    i = 1
    while True:
        tmp = num - i *i
        if tmp <0:
            print(False)
            return
        else:
            if tmp - math.sqrt(tmp) * math.sqrt(tmp) == 0:
                print(True)
                return
            else:
                i += 1

solve()
