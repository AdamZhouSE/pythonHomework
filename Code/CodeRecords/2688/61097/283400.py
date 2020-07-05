def dfs(i,tmp):
    if(i>n or tmp>g): return
    if(i==n):
        if(tmp==g): ans[0]+=1
        return
    #print(i,tmp)
    if(tmp==g):
        #print(i)
        ans[0]+=1
        return
    dfs(i+1,tmp)
    dfs(i+1,tmp+arr[i])

t=int(input())
while t>0:
    t-=1
    n=int(input())
    arr=input().split()
    arr=list(map(int,arr))
    g=int(input())
    ans=[0]
    dfs(0,0)
    print(ans[0])

    