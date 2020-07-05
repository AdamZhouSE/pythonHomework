import math


def func():
    test_num = int(input())
    i = 0
    while i < test_num:
        print(int(math.pow(int(input()), 1 / 3)))
        i += 1


func()
