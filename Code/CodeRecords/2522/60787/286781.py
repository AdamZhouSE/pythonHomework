arr1=eval(input())
arr2=eval(input())
re=[]
for i in arr2:
    while i in arr1:
        re.append(i)
        arr1.remove(i)
arr1=sorted(arr1)
re=re+arr1
print(re)