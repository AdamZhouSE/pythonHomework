n=int(input())
arr=list(map(int,input().split()))
ans=1
desk=1
for i in range(1,len(arr)):
    desk+=1
    if(arr[i] in arr[:i]):
        desk-=2
    ans=max(desk,ans)
print(ans)