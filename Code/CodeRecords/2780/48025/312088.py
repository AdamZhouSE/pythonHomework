t=int(input())
for i in range(0,t):
    n=int(input())
    arr=list(map(int,input().split()))
    k=int(input())
    product=arr[0]
    for j in range(1,len(arr)):
        product*=arr[j]
    print(product%k)