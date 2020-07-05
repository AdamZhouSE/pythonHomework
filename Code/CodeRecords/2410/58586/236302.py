arr=list(map(int,input().split(",")))
target=int(input())
res=1
for i in range(len(arr)):
    count=1
    start=arr[i]
    for j in range(i+1,len(arr)):
        if arr[j]-start==target:
            count+=1
            start=arr[j]
    res=max(res,count)
print(res)