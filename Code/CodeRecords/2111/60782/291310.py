"""
题目描述
    编写一个程序，找出第 n 个丑数。
    丑数就是只包含质因数 2, 3, 5 的正整数。
"""


def findKthUgly(k):
    count = 0
    n = 1
    while True:
        if isUgly(n):
            count += 1
        if count == k:
            return n
        else:
            n += 1


def isUgly(number):
    while number % 2 == 0:
        number = number / 2
    while number % 3 == 0:
        number = number / 3
    while number % 5 == 0:
        number == number / 5
    if number == 1:
        return True
    else:
        return False


print(findKthUgly(int(input())))
