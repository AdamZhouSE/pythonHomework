a = int(input())
b = 0
while (26 ** b) <= a:
    b += 1
b -= 1
while b > 0:
    print(chr(a // (26 ** b) + ord("A") - 1), end="")
    a %= (26 ** b)
    b -= 1
print()