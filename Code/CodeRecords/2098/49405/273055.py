a = int(input())
b = 1
while b < a:
    b *= 26
for i in range(b, 0, -1):
    print(chr(a // b + ord("A") - 1), end="")
    a %= b
    b //= 26
if a > 0: print(chr(a + ord("A") - 1))
else: print()