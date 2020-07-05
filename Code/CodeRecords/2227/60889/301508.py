def dfs(node,seen,res,k):
    for i in map(str,range(k)):
        nei = node + i
        if nei not in seen:
            seen.add(nei)
            dfs(nei[1:],seen,res,k)
            res.append(i)
    
seen = set()
res = []
n = int(input())
k = int(input())
a = "" 
for i in range(n-1):
    a = a + "0"
dfs(a,seen,res,k)
res.reverse()
print("".join(res)+a)