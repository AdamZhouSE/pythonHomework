n = int(input())
a = int(input())
b = int(input())
i = min(a, b)
while True:
    if i % a == 0 or i % b == 0:
        n -= 1
    if n == 0:
        break
    i += 1
print(i % 1000000007)
