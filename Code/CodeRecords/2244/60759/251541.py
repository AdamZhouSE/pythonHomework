from math import sqrt


def isprime(n):
    up = int(sqrt(n)) + 1
    for i in range(2, up):
        if n % i == 0:
            return False
    return True


bound = int(input())
num = bound
while True:
    n_str = str(num)
    if n_str == ''.join(reversed(n_str)) and isprime(num):
        print(num)
        break
    num += 1
