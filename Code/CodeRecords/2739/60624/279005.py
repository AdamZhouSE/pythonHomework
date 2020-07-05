def func15():
    temp = list(input().split(","))
    k = int(temp[0])
    n = int(temp[1])
    def dfs(i,n,path):
        if n == 0 and len(path) == k:
            ans.append(path)
        if n <= 0:
            return
        for j in range(i+1, 10):
            dfs(j, n-j, path+[j])

    ans = []
    dfs(0, n, [])
    print(ans)
    return
func15()