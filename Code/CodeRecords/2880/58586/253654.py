[k,n]=list(map(int,input().split(" ")))
arr=list(map(int,input().split(" ")))
left=-1
for i in range(len(arr)):
    if arr[i]>n:
        left=i
        break
right=left
for i in range(len(arr)-1,-1,-1):
    if arr[i]>n:
        right=i
        break
if left==-1:
    print(k)
else:
    print(k-(right-left+1))

