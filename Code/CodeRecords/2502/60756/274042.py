n=int(input())
arr=[]
ans=0
for i in range(n):
    arr.append(int(input()))
for i in range(1,n):
    ans+=max(arr[i-1],arr[i])
print(ans)