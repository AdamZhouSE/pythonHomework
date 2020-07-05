length=input().split()
array1=input().split()
array2=input().split()
result=[]
for item in array1:
    if array2.count(item)!=0:
        result.append(item)
print(' '.join(result))