arr1=list(map(int,input().split(",")))
arr2=list(map(int,input().split(",")))
res=0
for i in range(len(arr1)):
    for j in range(len(arr2)):
        res=max(res,abs(arr1[i]-arr1[j])+abs(i-j)+abs(arr2[j]-arr2[i]))
print(res)