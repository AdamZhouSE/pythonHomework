arr1=list(eval(input()))
arr2=list(eval(input()))
res=0
for i in range(len(arr1)):
    for j in range(len(arr1)):
        temp=abs(int(arr1[i])-int(arr1[j]))+abs(int(arr2[i])-int(arr2[j]))+abs(i-j)
        res=max(res,temp)
print(res)