import numpy as np

for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            if a[i] == k + a[j]:
                ans += 1
    print(ans)