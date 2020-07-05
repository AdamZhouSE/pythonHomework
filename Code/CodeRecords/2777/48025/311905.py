t=int(input())
for i in range(0,t):
    n=int(input())
    arr=list(map(int,input().split()))
    arr=sorted(arr)
    if n%2==0:
        print(int((arr[int(n/2)]+arr[int(n/2)-1])/2))
    else:
        print(int(arr[int(n/2)]))