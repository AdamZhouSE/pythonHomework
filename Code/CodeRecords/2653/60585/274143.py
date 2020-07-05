t=eval(input())
for _ in range(t):
    arr=list(map(int,input().strip().split(' ')))
    n=arr[0]
    x=arr[1]
    interval=min(10-x,10)
    time=(n-1)*interval
    print(time)