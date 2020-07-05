def func6(arr):
    live1=live2=0
    for i in range(len(arr)):
        if arr[i][0]=='1':
            live1=live1+int(arr[i][1])-int(arr[i][2])
        else:
            live2=live2+int(arr[i][1])-int(arr[i][2])
    if live1>=0:
        print("LIVE")
    else:
        print("DEAD")
    if live2>=0:
        print("LIVE")
    else:
        print("DEAD")

nums=int(input())
arr=[]
for i in range(nums):
    arr.append(input().split(" "))
func6(arr)
    