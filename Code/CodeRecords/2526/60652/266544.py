arr1=list(map(int,input().replace('[','').replace(']','').split(',')))
arr2=list(map(int,input().replace('[','').replace(']','').split(',')))
a=arr1+arr2
a.sort()
print(a)