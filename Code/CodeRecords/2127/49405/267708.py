a = int(input())
b = int("".join(input().split(",")))
r = 1
base = a % 1337
while b > 0:
    if b & 1 == 1: r = (r * base) % 1337
    base = (base * base) % 1337
    b >>= 1
print(r)