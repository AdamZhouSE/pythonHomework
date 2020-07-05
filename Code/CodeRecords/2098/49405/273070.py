n = int(input()) - 1
if n == 0:
    print("A")
    exit()
s = []
while n > 0:
    s.append(n % 26)
    n //= 26
print("".join(map(str, s)))