arr1=eval(input())
arr2=eval(input())
result=[]
a=[]
for i in range(len(arr2)):
    for j in range(len(arr1)):
        if(arr1[j]==arr2[i]):
            result.append(arr1[j])
for i in arr1:
    if(i not in arr2):
        a.append(i)
a=sorted(a)
result.extend(a)
print(result)