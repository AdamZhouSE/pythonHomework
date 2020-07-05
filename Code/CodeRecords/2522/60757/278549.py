arr1=sorted(eval(input()))
arr2=eval(input())
li=[]
for i in range(len(arr2)):
    k=arr1.count(arr2[i])
    for j in range(k):
        li.append(arr2[i])
for i in range(len(arr1)):
    if li.count(arr1[i])==0:
        k=arr1.count(arr1[i])
        for j in range(k):
            li.append(arr1[i])
print(li)
        