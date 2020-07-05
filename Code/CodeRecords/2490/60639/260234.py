arr1=sorted(eval(input()))
arr2=sorted(eval(input()))
result=[]
for i in range(len(arr1)):
    j=0
    while j<len(arr2) :
        if arr1[i]==arr2[j]:
            arr2.remove(arr1[i])
            result.append(arr1[i])
            j+=1
        else:
            j+=1
            continue
print(result)