cases=int(input())
def dfs(now):
    l=len(child[now])
    ans = 1
    for i in range(0,l):
        tmp=dfs(child[now][i])
        if tmp==-1 or tmp>k:
            return -1
        if tmp==k:
            continue
        ans+=tmp
    return ans
for c in range(cases):
    info=input().split()
    n=int(info[0])
    k=int(info[1])
    tree=[1 for i in range(2*n)]
    child=[[]for i in range(2*n)]
    for i in range(n-1):
        info=input().split()
        fa=int(info[0])-1
        ch=int(info[1])-1
        child[fa].append(ch)
    pairs=dfs(0)
    if pairs!=k:
        print('NO')
    else:
        print('YES')