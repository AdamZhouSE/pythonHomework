ar = list(map(int, input().split(',')))
n = len(ar)
ar.sort(reverse=True)  # 从大到小排序

ans=[]
dp = [1] * n
parent = [-1] * n

largest = 0
index = -1
for i in range(1, n):
    for j in range(0, i):
        if ar[j] % ar[i] == 0:
            if dp[j] + 1 >= dp[i]:
                dp[i] = dp[j] + 1
                parent[i] = j
    if largest < dp[i]:
        largest = dp[i]
        index = i

while index>=0:
    ans.append(ar[index])
    index=parent[index]


print(ans)