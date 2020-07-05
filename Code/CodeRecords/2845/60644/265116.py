n=int(input())
arr=[]
for i in range(0,n):
    arr=arr+[input().split()]
res=False
for i in range(0,n):
    for j in range(i+1,n):
        if int(arr[i][0])<int(arr[j][0]) and int(arr[i][1])>int(arr[j][1]):
            res=True
            break
if res:
    print('Happy Alex')
else:
    print('Poor Alex')
