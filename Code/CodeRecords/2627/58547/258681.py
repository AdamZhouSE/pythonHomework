from math import sqrt


def func():
    test_num = int(input())
    i = 0
    while i < test_num:
        p, s = [int(x) for x in input().split()]
        length = (p - sqrt((p * p) - (24 * s))) / 12
        height = (p / 4) - (2 * length)
        v = length * length * height
        print("%.5f" % v)
        i += 1


func()
