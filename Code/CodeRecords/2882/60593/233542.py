n=int(input())
arr=list(map(int,input().split()))
p1=True
p2=True
p3=True
pr=arr[0]
l1=0
l3=len(arr)-1
for i in range(len(arr)-1):
    if(arr[i]==arr[i+1]):
        l1=i
        break
for i in range(len(arr)-1,0,-1):
    if(arr[i]==arr[i-1]):
        l3=i
        break
if(l3-l1+1==n):
    p2=True
    l1=int(n/2)
    l3=int(n/2)
for i in range(l1,l3):
    if(arr[i]!=arr[i+1]):
        p2=False
for i in range(0,l1-1):
    if(arr[i]>arr[i+1]):
        p1=False
for i in range(l3,len(arr)-1):
    if(arr[i]<arr[i+1]):
        p3=False
if(p1==True and p2==True and p3==True):
    print('YES')
else:
    print('NO')