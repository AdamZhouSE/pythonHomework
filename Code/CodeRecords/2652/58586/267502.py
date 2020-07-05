[n,c,f]=list(map(int,input().split(" ")))
stu=[]
for i in range(c):
    stu.append(list(map(int,input().split(" "))))
stu.sort(key=lambda x:x[0],reverse=True)
ans=[]
def dfs(temp,sum,start):
    if len(temp)==n:
        if sum<f:
            ans.append(temp.copy())
            return True
        else:
            return False
    for i in range(start,c):
        temp.append(stu[i][0])
        if dfs(temp,sum+stu[i][1],i+1):
            return True
        temp.pop()
    return False
res=dfs([],0,0)
if not res:
    print(-1,end="")
else:
    print(ans[0][n//2],end="")