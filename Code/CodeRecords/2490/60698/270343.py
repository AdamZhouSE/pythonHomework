arr1=list(eval(input()))
arr2=list(eval(input()))
res=[]
for i in range(0,len(arr1)):
    if arr1[i] in arr2:
        res.append(arr1[i])
res.sort()
print(res)