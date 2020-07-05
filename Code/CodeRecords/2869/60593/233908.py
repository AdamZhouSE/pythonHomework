n=int(input())
arr=list(map(int,input().split()))
print(arr)
vis=[0 for i in range(1001)]
ans=[]
arr.reverse()
for i in range(len(arr)):
    if(vis[i]==0):
        ans.append(arr[i])
        vis[i]=1
print(ans)
print(len(ans))
for i in range(len(ans)):
    if(i==len(ans)-1):
        print(ans[i])
    else:
        print(ans[i],'',end='')