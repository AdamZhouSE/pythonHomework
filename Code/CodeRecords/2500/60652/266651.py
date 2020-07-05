#用例有问题
arr1=list(map(int,input().replace('[','').replace(']','').split(',')))
arr2=list(map(int,input().replace('[','').replace(']','').split(',')))
for index in arr2:
    tmp=arr1[0:index]
    tmp.reverse()
    arr1=tmp+arr1[index:]
print(arr1)