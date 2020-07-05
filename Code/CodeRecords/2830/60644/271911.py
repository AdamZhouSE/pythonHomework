p=input().split()
b=int(p[0])
k=int(p[1])
arr=input().split()
for i in range(0,k):
    arr[i]=int(arr[i])
if b%2==0:
    if arr[k-1]%2==0:
        print('even')
    else:
        print('odd')
else:
    if sum(arr)%2==0:
        print('even')
    else:
        print('odd')