def shuzi(n, k):
    seen = set()
    res = []
    def dfs(node):
        for x in map(str, range(k)):
            nei = node + x
            if nei not in seen:
                seen.add(nei)
                dfs(nei[1:])
                res.append(x)
    dfs('0'*(n-1))
    return ''.join(res) + '0'*(n-1)
n=int(input())
k=int(input())
a=shuzi(n,k)
a=a[::-1]
print(a)