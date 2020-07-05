num = int(input())

while num % 5 == 0:
    num = num // 5

while num % 3 == 0:
    num //= 3

while num % 2 == 0:
    num //= 2

print(num == 1)
