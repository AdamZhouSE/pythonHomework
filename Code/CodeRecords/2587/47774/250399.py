num=eval(input())
arr=[]
for i in range(num):
    str=input().split(",")
    arr.append(str)
res=0
for i in range(1,len(arr)):
    dy = abs(int(arr[i][1])-int(arr[i-1][1]))
    dx = abs(int(arr[i][0])-int(arr[i-1][0]))
    res=res+max(dy,dx)
print(res)