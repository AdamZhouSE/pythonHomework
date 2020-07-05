arr1=input()[1:-1].split(",")
arr2=input()[1:-1].split(",")
for i in range(len(arr2)):
    arr2[i]=int(arr2[i])
for i in range(len(arr1)):
    arr1[i]=int(arr1[i])
res=[]
rest=[]
for e in arr2:
    for i in range(len(arr1)):
        if arr1[i]==e:
            res.append(e)
for e in arr1:
    if e not in res:
        rest.append(e)
rest.sort()
res.extend(rest)
print(res)