n = int(input())
while n % 2 == 0:
    n = n // 2

while n % 3 == 0:
    n = n // 3

while n % 5 == 0:
    n = n // 5

print(n == 1)