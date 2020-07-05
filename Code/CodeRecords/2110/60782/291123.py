"""
题目描述
    编写一个程序判断给定的数是否为丑数。
    丑数就是只包含质因数 2, 3, 5 的正整数。
"""
n = int(input())
primes = []
for j in range(2, n):
    is_prime = True
    for k in range(2, j):
        if j % k == 0:
            is_prime = False
    if is_prime:
        primes.append(is_prime)
answer = True
for i in primes:
    if n % i == 0 and (i != 2 or i != 3 or i != 5):
        answer = False
print(answer)
