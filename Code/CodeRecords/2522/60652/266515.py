arr1=list(map(int,input().replace('[','').replace(']','').split(',')))
arr2=list(map(int,input().replace('[','').replace(']','').split(',')))
a=[]
for i in arr2:
    while i in arr1:
        a.append(i)
        arr1.pop(arr1.index(i))
arr1.sort()
a+=arr1
print(a)