import math
"""
请你帮忙给从 1 到 n 的数设计排列方案，使得所有的「质数」都应该被放在「质数索引」（索引从 1 开始）上；你需要返回可能的方案总数
让我们一起来回顾一下「质数」：质数一定是大于 1 的，并且不能用两个小于它的正整数的乘积来表示
由于答案可能会很大，所以请你返回答案 模 mod 10^9 + 7 之后的结果即可
"""

def get_prime_num(n):
    num=0
    for i in range(n):
        if (i+1)==1:
            judge=False
        elif (i+1)==2 or (i+1)==3:
            judge=True
        else:
            judge=True
            for m in range(2, math.floor((i+1) ** 0.5) + 1):
                if (i+1) % m == 0:
                    judge = False
        if judge:
            num+=1
    return num


def get_Factorial(n):
    result=1
    for i in range(n):
        result=result*(i+1)
    return result


n=int(input())

prime_num=get_prime_num(n)
result=(get_Factorial(prime_num)*get_Factorial(n-prime_num))%(10**9+7)
print(result)