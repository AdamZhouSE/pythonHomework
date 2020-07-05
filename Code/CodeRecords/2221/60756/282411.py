def BFS(arr:list,tag:list,s:int,e:int)->bool:
    ans=[s]
    count=0
    while count<len(ans):
        loc=tag.index(ans[count])
        for i in range(len(tag)):
            if arr[loc][i]==1 and tag[i] not in ans:
                ans.append(tag[i])
        count+=1
    return e in ans

N,M=map(int,input().split())
tag=[i for i in range(1,N+1)]
arr=[[0 for i in range(N)] for j in range(N)]
for i in range(M):
    x,y=map(int,input().split())
    arr[x-1][y-1]=1
ans=N
for i in tag:
    for j in tag:
        if i!=j:
            if not BFS(arr,tag,j,i):
                ans-=1
                break
print(ans)