n = int(input()) - 1
if n == 0:
    print("A")
    exit()
s = []
while n > 0:
    s.append(chr(n % 26 + 65))
    n //= 26
print("".join(s))