'''
请你帮忙给从 1 到 n 的数设计排列方案，使得所有的「质数」都应该被放在「质数索引」（索引从 1 开始）上；你需要返回可能的方案总数。
让我们一起来回顾一下「质数」：质数一定是大于 1 的，并且不能用两个小于它的正整数的乘积来表示。
由于答案可能会很大，所以请你返回答案 模 mod 10^9 + 7 之后的结果即可。
'''

import math

n = int(input())

def isPrime(a):
    for i in range(2, int(a ** 0.5) + 1):
        if(a % i == 0):
            return False
    return True

count = 1
if (n == 1 or n == 2):
    print('1')
else:
    for i in range(3, n):
        if(isPrime(i)):
            count += 1
    res = (math.factorial(count) * math.factorial(n - count)) % (10 ** 9 + 7)
    print(res)