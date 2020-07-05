a = int(input())
b = 1
while b <= a:
    b *= 26
b //= 26
while b > 0:
    print(chr(a // b + ord("A") - 1), end="")
    a %= b
    b //= 26
print()