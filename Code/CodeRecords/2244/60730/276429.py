# 数学规律1：除 11 外的偶数位回文数，都能被 11 整除
# 数学规律2：除 2 和 3 外，所有的素数一定在 6 的两侧

import math

N = int(input())


def isPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0 or n == 1:
            return False
    return True


def isPalindrome(m):
    tmp = list(map(int, str(m)))
    if len(tmp) == 1 or m == 11:
        return True
    if (len(tmp) % 2) == 0:
        return False
    else:
        for j in range(int(len(tmp) / 2)):
            if tmp[j] != tmp[len(tmp) - 1 - j]:
                return False
    return True


m = N
while m < int(2 * pow(10, 8)):
    if isPalindrome(m) and isPrime(m):
        print(m)
        exit()
    else:
        m = m + 1
