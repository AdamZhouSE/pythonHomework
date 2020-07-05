def dfs(n,k):
    if cache[n][k-1]!=-1:
        return cache[n][k-1]
    if n==0 or n == 1 or k==1:
        cache[n][k-1]=n
        return n
    temp = n
    for i in range(1,n+1):
        t = max(dfs(i-1,k-1),dfs(n-i,k))
        temp = min(temp,1+t)
    cache[n][k-1]=temp
    return temp
k = int(input())
n = int(input())
cache = [[-1 for i in range(k)]for j in range(n+1)]
if k==0:
    print(0)
else:
    print(dfs(n,k))