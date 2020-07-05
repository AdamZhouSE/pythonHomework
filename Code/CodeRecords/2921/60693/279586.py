def oprTimes(arr:[int],d:int):
    arrlen=len(arr)
    for i in range(arrlen-1):
        diff=arr[i+1]-arr[i]
        if diff%d:
            return -1
    res=0
    middleNum=arr[arrlen//2]
    for x in arr:
        if x!=middleNum:
            res+=abs(x-middleNum)//d
    return res


nmd=input().split()
n,m,d=int(nmd[0]),int(nmd[1]),int(nmd[2])
arr=[]
for _ in range(n):
    row=list(map(int,input().split()))
    for num in row:
        arr.append(num)
arr.sort()
print(oprTimes(arr,d))