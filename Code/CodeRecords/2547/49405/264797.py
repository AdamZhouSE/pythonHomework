import numpy as np

for t in range(int(input())):
    n = int(input())
    a = sorted(list(map(int, input().split())))
    k = int(input())
    ans = []
    for i in range(n):
        for j in range(i + 1, n):
            if a[i] - a[j] == -k:
                if not a[i] in ans:
                    ans.append(a[i])
    print(len(ans))