arr1=eval(input())
arr2=sorted(arr1)
result=len(arr1)
for i in range(0,len(arr1)):
    if arr1[i]==arr2[i]:
        result-=1
    else:
        break
for i in range(0,len(arr1)):
    if arr1[len(arr1)-1-i]==arr2[len(arr1)-1-i]:
        result-=1
    else:
        break
print(result)