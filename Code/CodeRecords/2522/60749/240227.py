arr1=input()
arr2=input()
res1=[]
res2=[]
for x in arr2:
    res2.append(res1)
for t in arr1:
    for x in range(0,len(arr2)):
        if t==arr2[x]:
            res2[x].append(t)
res3=[]
for t in arr1:
    if not t in arr2:
        res3.append(t)
res3=sorted(res3)   
result=[]
for t in res2:
    for k in t:
        result.append(k)
result=result+res3
print(result)
