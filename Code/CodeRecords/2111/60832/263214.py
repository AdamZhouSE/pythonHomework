n = int(input())

x = 2
i = 1

while i < n:
    num = x
    while num % 5 == 0:
        num = num // 5

    while num % 3 == 0:
        num //= 3

    while num % 2 == 0:
        num //= 2

    if num == 1:
        i += 1

    x += 1

print(x - 1)