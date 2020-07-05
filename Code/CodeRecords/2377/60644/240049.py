num=int(input())
arr=[]
for i in range(0,num):
    arr=arr+[input()]
x=int(arr[0][0:1])-int(arr[1][0:1])
y=int(arr[0][2:3])-int(arr[1][2:3])
res=False
for i in range(2,num):
    x1=int(arr[0][0:1])-int(arr[i][0:1])
    y1=int(arr[0][2:3])-int(arr[i][2:3])
    if x*y1!=x1*y:
        res=True
        break
print(res)