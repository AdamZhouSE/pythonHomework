array1=list(map(int,input()[1:-1].split(",")))
array2=list(map(int,input()[1:-1].split(",")))
res=[]
array=[]
temp=[]
for i in range(0,len(array2)):
    for j in range(0,len(array1)):
        if array1[j]==array2[i]:
            res.append(array1[j])
            array.append(j)
k=0
array.sort()
for i in range(0,len(array1)):
    if k==len(array)or i!=array[k]:
        temp.append(array1[i])
    else:
        k=k+1
temp.sort()
for i in range(0,len(temp)):
    res.append(temp[i])
print(res)