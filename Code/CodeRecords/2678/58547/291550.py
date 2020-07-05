import math


def func():
    test_num = int(input())
    i = 0
    while i < test_num:
        number = int(input())
        power = math.log2(number)
        if 2 ** int(power) != number:
            print(-1)
    
        else:
            print(int(power + 1))
        i += 1


func()
