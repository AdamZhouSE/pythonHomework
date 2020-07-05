import math


def cal(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return math.pow(10, n) + 10 * cal(n - 1)


def resolve(n):
    if n == "":
        return 0
    if len(n) == 1:
        if "0" != n:
            return 1
        else:
            return 0
    res = cal(len(n) - 1)
    if n.startswith("1"):
        return res + int(n[1:]) + 1 + resolve(n[1:])
    else:
        return res + int(math.pow(10, len(n) - 1)) - 1 + int(n[0])*resolve(n[1:])


num = input()
print(resolve(num))