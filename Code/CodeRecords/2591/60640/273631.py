"""
对于每个数n
n+2是素数
"""


def is_prime(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


t = int(input())
for j in range(t):
    n = int(input())
    if is_prime(n+2):
        print("Yes")
    else:
        print("No")
