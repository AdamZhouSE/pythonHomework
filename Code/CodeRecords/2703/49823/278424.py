def h(m):
    n=len(m)
    visited=[0]*n
    r=0
    def dfs(i):
        for j in range(n):
            if m[i][j] and visited[j]==0:
                visited[j]=1
                dfs(j)
    for i in range(n):
        if visited[i]==0:
            dfs(i)
            r+=1
    print(r)

if __name__ == '__main__':
    h(eval(input()))