arr1=input()[1:-1].split(',');arr1=[int(x) for x in arr1]
arr2=input()[1:-1].split(',');arr2=[int(x) for x in arr2]
res=[]
#print(arr1,arr2)
for i in range(len(arr2)):
    for j in range(arr1.count(arr2[i])):
        arr1.remove(arr2[i])
        res.append(arr2[i])
arr1.sort()
res.extend(arr1)
print(res)