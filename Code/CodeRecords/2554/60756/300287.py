n=int(input())
flag=False
arr=[[-1,-1,-1]]
for i in range(n):
    x,y=map(int,input().split())
    arr.append([x,y,0])
arr.sort(key=lambda x:x[0])
last=0
L=0
for i in range(1,n+1):
    if arr[i][1]<=last:flag=True
    else:
        temp=min(arr[i][1]-arr[i][0],arr[i][1]-last)
        L+=temp
        arr[i][2]=temp
        if arr[i][0]<last:
            arr[i-1][2]-=last-arr[i][0]
        last=arr[i][1]
dec=float("Inf")
for i in range(1,n+1):
    dec=min(dec,arr[i][2])
if flag:
    print(L,end='')
else:
    print(L-dec,end='')