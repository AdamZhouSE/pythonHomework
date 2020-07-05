# 21
arr1=list(eval(input()))
arr2=list(eval(input()))
result=[]
for i in range(0,len(arr2)):
    count=arr1.count(arr2[i])
    for j in range(0,count):
        result.append(arr2[i])
        arr1.remove(arr2[i])
result=result+sorted(arr1)
print(result)