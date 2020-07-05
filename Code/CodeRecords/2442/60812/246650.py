s = [int(i) for i in input()[1:-1].split(',')]
m = 0
s.sort()
for i in range(1, len(s)):
    m = max(m, s[i]-s[i-1])
print(m)