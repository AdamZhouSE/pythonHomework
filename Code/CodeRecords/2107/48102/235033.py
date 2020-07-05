def is2exp2():
    num = int(input())
    return num & (num - 1) == 0


print(is2exp2())