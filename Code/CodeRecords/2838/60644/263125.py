n=int(input())
arr=input().split()
for i in range(0,n):
    arr[i]=int(arr[i])
for i in range(0,n):
    for j in range(0,n-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
res=0
for i in range(0,int(n/2)):
    res=res+(arr[i]+arr[n-1-i])*(arr[i]+arr[n-1-i])
print(res)
