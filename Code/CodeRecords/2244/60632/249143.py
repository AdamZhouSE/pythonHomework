import math


def is_prime_number(x: int) -> bool:
    if x == 2:
        return True
    for i in range(2, math.ceil(math.sqrt(x) + 1)):
        if x % i == 0:
            return False
    return True


def is_palindrome(x: int) -> bool:
    x = list(str(x))
    tmp = x[:]
    tmp.reverse()
    return tmp == x


n = int(input())
end = False
result = 0
while True:
    if is_prime_number(n) and is_palindrome(n):
        result = n
        end = True
    n += 1
    if end:
        break
print(result)
