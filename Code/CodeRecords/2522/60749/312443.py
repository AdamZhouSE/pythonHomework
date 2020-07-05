arr1=input()
arr2=input()
arr1=arr1[1:len(arr1)-1]
arr2=arr2[1:len(arr2)-1]
arr1=list(map(int, arr1.split(",")))
arr2=list(map(int, arr2.split(",")))
res1=[]
res2=[]


for x in arr2:
    res2.append(0)

for t in arr1:
    for x in range(0,len(arr2)):
        if t==arr2[x]:
            res2[x]+=1

res3=[]
for t in arr1:
    if not t in arr2:
        res3.append(t)
res3=sorted(res3)
result=[]
for t in range(0,len(res2)):
    for k in range(0,res2[t]):
        result.append(arr2[t])
result=result+res3
print(result)