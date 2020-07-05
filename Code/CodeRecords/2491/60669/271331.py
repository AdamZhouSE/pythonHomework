arr1=eval(input())
arr2=eval(input())
if len(arr1)<len(arr2):
    x=arr1
    y=arr2
else:
    x=arr2
    y=arr1
result=[]
for item in x:
    if item in y:
        result.append(item)
result.sort()
print(result)