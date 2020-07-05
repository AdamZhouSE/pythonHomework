n=int(input())
arr=input().split()
for i in range(0,n):
    arr[i]=int(arr[i])
max=0
b=[]
b=[]+arr
for i in range(0,n+1):
    for j in range(0,n-i+1):
        for k in range(j,j+i):
            if arr[k]==1:
                arr[k]=0
            else:
                arr[k]=1
            if arr.count(1)>max:
                max=arr.count(1)
        arr=[]+b
print(max)
