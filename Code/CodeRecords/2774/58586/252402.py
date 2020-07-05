nums=int(input())
for i in range(nums):
    [n,cost]=list(map(int,input().split(" ")))
    arr=list(map(int,input().split(" ")))
    arr.sort()
    sum=0
    index=0
    for j in range(n):
        sum+=arr[j]
        if sum>cost:
            index=j
            break
    if sum>cost:
        print(index)
    else:
        print(n)