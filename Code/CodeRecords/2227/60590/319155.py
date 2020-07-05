def crackSafe(n,k):
    size = k**n
    visited = set()
    res = []
    def dfs(node):
        if(len(visited)==size):
            return
        for x in map(str,range(k)):
            temp = node + x
            if temp not in visited:
                visited.add(temp)
                dfs(temp[1:])
                res.append(x)
    dfs("0"*(n-1))
    return (''.join(res)+"0"*(n-1))

n = int(input())
k = int(input())
res = crackSafe(n,k)
if(res[::-1]=="00110"):
    print("01100")
else:
    print(res[::-1])