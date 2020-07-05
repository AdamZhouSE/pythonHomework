arr1=eval(input())
arr2=eval(input())
li=[]
for i in range(len(arr1)):
    for j in range(len(arr2)):
        if arr1[i]==arr2[j]:
            li.append(arr1[i])
li=list(tuple(set(li)))
print(sorted(li))