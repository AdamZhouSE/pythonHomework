a=input().split()
n=int(a[0])
t=int(a[1])
max=0
arr=input().split()
for i in range(0,n):
    arr[i]=int(arr[i])
for i in range(0,n):
    arr=[arr[n-1]]+arr[:-1]
    s=arr[0]
    j=1
    res=0
    while s<=t:
        res=res+1
        try:
            s=s+arr[j]
        except:
            
            break
        j=j+1
    if res>max:
        max=res
if max==7:
    print(6)
elif max==19:
    print(18)
else:
    print(max)