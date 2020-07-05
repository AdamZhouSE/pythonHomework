s = input()
m = int(s[1])
n = int(s[3])
while n > m:
    n &= n - 1
print(n)

