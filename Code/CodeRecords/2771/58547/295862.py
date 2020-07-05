import math


def func():
    test_num = int(input())
    i = 0
    while i < test_num:
        number = int(input())
        if int(math.sqrt(number)) ** 2 == number:
            print(1)
        else:
            print(0)
        i += 1


func()
