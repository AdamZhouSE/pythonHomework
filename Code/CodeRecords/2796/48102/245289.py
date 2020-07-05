import math


def large(n: int, ls: list) -> int:
    big = - 2 ** 31
    for i in range(n):
        if (ls[i] < 0 or math.sqrt(ls[i]) != int(math.sqrt(ls[i]))) and ls[i] > big:
            big = ls[i]
    return big


num = int(input())
lst = input().split(' ')
lst = list(map(int, lst))
print(large(num, lst))
