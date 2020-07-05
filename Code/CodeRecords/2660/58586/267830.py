nums=int(input())
arr=[]
for i in range(nums):
    order=list(map(str,input().strip().split(" ")))
    if order[0]=="T":
        arr.append(order[1])
    elif order[0]=="U":
        for i in range(int(order[1])):
            arr.pop()
    elif order[0]=="Q":
        print(arr[int(order[1])-1])
