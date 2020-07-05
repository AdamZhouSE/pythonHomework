"""
题目描述
    编写一段程序来查找第 n 个超级丑数。
    超级丑数是指其所有质因数都是长度为 k 的质数列表 primes 中的正整数。
"""


def nthSuperUglyNumber(n, primes):
    """
    :type n: int
    :type primes: List[int]
    :rtype: int
    """
    if n < 0:
        return False
    t = len(primes) * [0]
    res = [1]
    while len(res) < n:
        m = pow(2, 32)
        for i in range(len(primes)):
            temp = res[t[i]] * primes[i]
            if temp < m:
                m = temp
        for j in range(len(primes)):
            if m == res[t[j]] * primes[j]:
                t[j] += 1
        res.append(m)
    return res[-1]


nn = int(input())
p = list(map(int, input().split(",")))
print(nthSuperUglyNumber(nn, p))