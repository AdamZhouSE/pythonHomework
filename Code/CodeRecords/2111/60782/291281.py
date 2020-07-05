"""
题目描述
    编写一个程序，找出第 n 个丑数。
    丑数就是只包含质因数 2, 3, 5 的正整数。
"""


def test(n):
    primes = []
    for j in range(2, n):
        is_prime = True
        for k in range(2, j):
            if j % k == 0:
                is_prime = False
        if is_prime:
            primes.append(j)
    answer = True
    # print(primes)
    for i in primes:
        if n % i == 0 and (i != 2 and i != 3 and i != 5):
            answer = False
    return answer


standard = int(input())
counter = 0
answer = -1
for i in range(2, 10000):
    if test(i):
        counter += 1
    if counter == standard - 1:
        answer = i
        break
print(answer)