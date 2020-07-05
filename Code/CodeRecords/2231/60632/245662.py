import math


def is_prime_number(x):
    for i in range(2, math.ceil(math.sqrt(x) + 1)):
        if x % i == 0:
            return False
    return True


t = int(input())
result = []
for i in range(t):
    n = int(input())
    prime = [2]
    is_sn = False
    # 要将一个数分解为三个不同质数的乘积，而两个不同质数的乘积最小为2*3=6
    # 故先找出小于n//6的所有质数，并在这些质数中判断是否有满足条件的三个
    for j in list(range(3, math.ceil(n / 6) + 1))[::2]:
        if is_prime_number(j):
            prime.append(j)
    for a in range(len(prime) - 2):
        for b in range(a + 1, len(prime) - 1):
            for c in range(b + 1, len(prime)):
                if prime[a] * prime[b] * prime[c] == n:
                    is_sn = True
                    result.append(1)
    if not is_sn:
        result.append(0)
for i in result:
    print(i)
