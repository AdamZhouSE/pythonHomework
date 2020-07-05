import math


def func():
    print(__import__("functools").reduce(math.gcd, [int(x) for x in input().split(",")]) == 1)


func()
