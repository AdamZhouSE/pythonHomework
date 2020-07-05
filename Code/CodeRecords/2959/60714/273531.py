import re

a = input()
b = input()
ans = 0
for i in range(0, len(a)):
    for j in range(i, len(a)):
        pattern = a[i: j + 1]
        ans += len(re.findall(pattern, b))
print(ans)
