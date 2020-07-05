t=int(input())
for _ in range(0,t):
    n=int(input())
    arr=input().split()
    arr=list(map(int,arr))
    index=-1
    for i in range(0,len(arr)):
        if arr.count(arr[i])!=1:
            index=i+1
            break
    print(index)