arr1=list(map(int,input().replace('[','').replace(']','').replace('Null','').split(',')))
arr2=list(map(int,input().replace('[','').replace(']','').replace('Null','').split(',')))
a=arr1+arr2
a.sort()
print(a)