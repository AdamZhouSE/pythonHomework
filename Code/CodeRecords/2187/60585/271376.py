t=eval(input())
for _ in range(t):
    num=list(map(int,input().strip().split(' ')))
    n=num[0]
    k=num[1]
    arr=list(map(int,input().strip().split(' ')))
    start,end=0,k-1
    maxSum=0
    temp=0
    for i in range(k):
        temp+=arr[i]
    maxSum=temp
    for end in range(k,n):
        temp-=arr[start]
        start+=1
        temp+=arr[end]
        maxSum=max(maxSum,temp)
    print(maxSum)