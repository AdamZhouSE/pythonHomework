T=int(input())
for i in range(T):
    arr=list(map(int,input().split()))
    N=int(input())
    d=arr[1]-arr[0]
    print(arr[1]+(N-2)*d)