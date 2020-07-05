length=int(input())
arr=input().split()
for i in range(0,length):
    arr[i]=int(arr[i])
res=-1
for i in range(0,length):
    ans=True
    for j in range(0,length):
        if arr[j]%arr[i]!=0:
            ans=False
            break
    if ans:
        res=arr[i]
        break
print(res)