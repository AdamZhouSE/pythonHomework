n=int(input())
arr=input().split()
for i in range(0,n):
    arr[i]=int(arr[i])
res=0
s1=sum(arr)
for i in range(0,n):
    for j in range(0,n-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
s2=0
for i in range(1,n,2):
    s2=s2+arr[i]
s2=s2*2
res=s2-s1
print(res)
