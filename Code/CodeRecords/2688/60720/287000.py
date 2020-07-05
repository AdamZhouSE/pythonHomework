size=int(input())
ans=[0]
def dfs(i,tmp):
    if i>=n or tmp>=t:
        if tmp==t:
            ans[0]+=1
        return
    dfs(i+1,tmp)
    dfs(i+1,tmp+lst[i])
for k in range(size):
    n=int(input())
    lst=input().split()
    lst=list(map(int,lst))
    t=int(input())
    ans=[0]
    dfs(0,0)
    print(ans[0])