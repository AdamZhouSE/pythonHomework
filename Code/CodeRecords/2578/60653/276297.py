import re
import math
s = list([int(n) for n in re.findall(r"\-?\d+", input())])
n = int(input())
ans = 0

for i in range(1, n):
    sum = 0
    for j in s:
        sum += math.ceil(j/i)
    if sum <= n:
        ans = i
        break
print(ans)