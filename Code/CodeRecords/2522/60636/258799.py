arr1=eval(input())
arr2=eval(input())
res=[]
for i in arr2:
    a=arr1.copy()
    for j in arr1:
        if(j==i):
            res.append(j)
            a.pop(a.index(j))
    arr1=a
arr1.sort()
for i in arr1:
    res.append(i)
print(res)