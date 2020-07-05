import math


def turnToBinary(x):
    result = ""
    while x != 0:
        remain = x % 2
        x = int(math.floor(x / 2))
        result = str(remain) + result
    return result


T = int(input())

for i in range(0, T):
    num = int(input())
    binary = turnToBinary(num)
    if binary.count("1") % 2 == 1:
        print("odd")
    else:
        print("even")
