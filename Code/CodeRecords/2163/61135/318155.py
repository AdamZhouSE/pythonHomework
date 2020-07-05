def factorial(num):
    res = [1]
    i = 1
    while i <= num:
        res.append(i * res[i - 1])
        i += 1
    return res
def DFS(visited, level, n, k, res):
    if(level==n):
        return res
    curr=factoriallist[n-1-level]
    for i in range(1,n+1):
        if visited[i]==1:
            continue
        if curr<k:
            k-=curr
            continue
        if(curr>=k):
            res+=str(i)
            visited[i]=1
            return DFS(visited,level+1,n,k,res)
n = int(input())
k = int(input())
factoriallist=factorial(n);
visited = [0 for a in range(n + 1)]
res=""
if n == 0:
    res=""
else:
    res=DFS(visited,0,n,k,"")
print(res)