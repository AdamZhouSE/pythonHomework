arr1=eval(input())
arr2=eval(input())
result=[]
for i in range(len(arr2)):
    index=arr2[i]
    n=arr1.count(index)
    for j in range(n):
        arr1.remove(index)
        result.append(index)
arr1.sort()
for i in range(len(arr1)):
    result.append(arr1[i])
print(result)