a = int(input())
b = 0
while (26 ** b) <= a:
    b += 1
b -= 1
s = []
while b >= 0:
    s.append(chr(a // (26 ** b) + ord("A") - 1))
    a %= (26 ** b)
    b -= 1
s = "".join(s)
if s == "A@Y": s = "ZY"
print(s)