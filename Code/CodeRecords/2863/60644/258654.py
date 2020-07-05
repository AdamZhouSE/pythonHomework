a=input().split()
n=int(a[0])
h=int(a[1])
arr=input().split()
for i in range(0,len(arr)):
    arr[i]=int(arr[i])
res=0
for i in range(0,len(arr)):
    if arr[i]>h:
        res=res+2
    else:
        res=res+1
print(res)
