s = list(input().strip())
s = [ord(i)-64 for i in s]
n = 0
t = 1
for i in s[::-1]:
    n += t * i
    t *= 26
print(n)