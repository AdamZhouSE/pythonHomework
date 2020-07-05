def is_prime(num):
    if num == 2:
        return True
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    return True


def is_pla(num):
    x = list(str(num))
    for i in range(0, len(x) // 2 + 1):
        if not x[i] == x[len(x) - 1 - i]:
            return False
    return True


n = int(input())
while True:
    if is_pla(n):
        if is_prime(n):
            break
    n += 1
print(n)
