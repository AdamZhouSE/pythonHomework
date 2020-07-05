n = 10 ** int(input())
ans = 0
for i in range(n):
    import numpy as np
    if len(np.unique(sorted(str(i)))) == len(str(i)):
        ans += 1
print(ans)