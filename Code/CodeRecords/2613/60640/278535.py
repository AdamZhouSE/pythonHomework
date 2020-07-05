"""
第i组数有i个，
i是偶数则i组中全是偶数，否则全为奇数
给定起始数1
一组中的数每次加2
换组时数加1
"""
ans = []
start = 1
for i in range(1, 20):
    for j in range(i):
        ans.append(start)
        if j < i-1:
            start += 2
        else:
            start += 1
t = int(input())
for i in range(t):
    n = int(input())
    for j in range(n-1):
        print(ans[j], end=" ")
    print(ans[n-1])
