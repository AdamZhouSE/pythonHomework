T=int(input())
for i in range(T):
    num=0
    n=int(input())
    arr=list(map(int,input().split()))
    high=arr.index(max(arr))
    left,right=0,0
    for j in range(high):
        if(arr[j]>left):
            left=arr[j]
        else:
            num+=left-arr[j]
    for j in range(n-1,high,-1):
        if(arr[j]>right):
            right=arr[j]
        else:
            num+=right-arr[j]
    print(num)