arr1=sorted(eval(input().strip()))
arr2=sorted(eval(input().strip()))
result=[]
i=j=k=0
while (i<len(arr1))&(j<len(arr2)):
    if arr1[i]==arr2[j]:
        result.append(arr1[i])
        i+=1
        j+=1
    elif arr1[i]<arr2[j]:
        i+=1
    else:
        j+=1
print(result)