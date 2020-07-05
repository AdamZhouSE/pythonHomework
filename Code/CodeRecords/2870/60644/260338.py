num=int(input())
arr=input().split()
for i in range(0,len(arr)):
    arr[i]=int(arr[i])
arr1=[]
arr2=[]
for i in range(0,len(arr)):
    if arr[i]%2==0:
        arr2=arr2+[arr[i]]
    else:
        arr1=arr1+[arr[i]]
for i in range(0,len(arr1)):
    for j in range(0,len(arr1)-1):
        if arr1[j]<arr[j+1]:
            temp=arr1[j]
            arr1[j]=arr1[j+1]
            arr1[j+1]=temp
res=0
if len(arr1)%2==0:
    for i in range(0,num):
        res=res+arr[i]
else:
    for i in range(0,len(arr1)-1):
        res=res+arr1[i]
    for i in range(0,len(arr2)):
        res=res+arr2[i]
print(res)
