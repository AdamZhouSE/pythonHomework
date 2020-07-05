arr1 = eval(input())
arr2 = eval(input())
result = []
for i in range(0,len(arr2)):
    for j in range(0,len(arr1)):
        if arr1[j]==arr2[i]:
            result.append(arr1[j])
temp = []
for m in range(0,len(arr1)):
    if arr1[m] not in result:
        temp.append(arr1[m])
temp = sorted(temp)
for n in range(0,len(temp)):
    result.append(temp[n])
print(result)