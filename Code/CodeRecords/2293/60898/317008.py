T=eval(input())
for i in range(0,T):
    N=eval(input())
    arr=input().split()
    for j in range(0,N):
        arr[j]=int(arr[j])
    K=eval(input())
    arr=sorted(arr)
    print(arr[K-1])
