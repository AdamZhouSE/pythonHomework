num=int(input())
arr=[]
for i in range(0,num):
    arr=arr+[input()]
k=(int(arr[0][0:1])-int(arr[1][0:1]))/(int(arr[0][2:3])-int(arr[1][2:3]))
res=True
for i in range(1,len(arr)):
    k1=(int(arr[0][0:1])-int(arr[i][0:1]))/(int(arr[0][2:3])-int(arr[i][2:3]))
    if k!=k1:
        res=False
        break
print(res)
