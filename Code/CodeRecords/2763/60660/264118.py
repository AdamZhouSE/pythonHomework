def dfs(l,c,n,m):
    sum=0
    if l>n or c>m:
        return 0
    elif l==n and c<=m:
        return 1
    else:
        c*=2
        while(c<=m):
            sum+=dfs(l+1,c,n,m)
            c+=1
    return sum
t=int(input())
for i in range(t):
    l=eval('['+input().replace(' ',',')+']')
    m=l[0]
    n=l[1]
    sum=0
    for j in range(1,m//2+1):
        sum+=dfs(1,j,n,m)
    print(sum)