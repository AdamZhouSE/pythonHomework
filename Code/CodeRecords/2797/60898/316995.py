days=eval(input())
arr=input().split()
for i in range(0,len(arr)):
    arr[i]=int(arr[i])
if len(arr)<=1 and arr[len(arr)-1]!=0:
    print(-1)
elif len(arr)<=1 and arr[len(arr)-1]==0:
    print('UP')
elif arr[len(arr)-1]-arr[len(arr)-2]>0 and arr[len(arr)-1]!=15:
    print('UP')
elif arr[len(arr)-1]==0:
    print('UP')
else:
    print('DOWN')