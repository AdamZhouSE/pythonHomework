n=int(input())
arr=list(map(int,input().split()))
vis=[0 for i in range(1001)]
ans=[]
arr.reverse()
for i in range(len(arr)):
    if(vis[arr[i]]==0):
        ans.append(arr[i])
        vis[arr[i]]=1
ans.reverse()
print(len(ans))
for i in range(len(ans)):
    if(i==len(ans)-1):
        print(ans[i])
    else:
        print(ans[i],'',end='')