a = int(input())
b = 1
while b < a:
    b *= 26
for i in range(b, -1, -1):
    print(chr(a // (26 ** b) + ord("A") - 1), end="")
    a %= 26