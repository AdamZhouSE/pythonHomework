n = int(input())
if n > 10:
    print(0)
    exit()
n = 10 ** n
ans = 0
for i in range(n):
    import numpy as np
    if len(np.unique(sorted(str(i)))) == len(str(i)):
        ans += 1
print(ans)