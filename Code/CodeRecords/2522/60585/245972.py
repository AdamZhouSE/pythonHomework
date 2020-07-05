import collections
arr1=eval(input())
arr2=eval(input())
s = collections.Counter(arr1)
profix=[]
res=[]
for i in range(len(arr2)):
    number=s[arr2[i]]
    for j in range(number):
        res.append(arr2[i])
for i in range(len(arr1)):
    if arr1[i] not in arr2:
        profix.append(arr1[i])
profix=sorted(profix)
res.extend(profix)
print(res)