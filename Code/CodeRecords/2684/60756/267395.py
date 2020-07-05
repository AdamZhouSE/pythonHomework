def dp(arr:list,N:int,J:bool)->int:
    if N==0:
        if J: return arr[0]
        else: return 0
    else:
        if J: return dp(arr,N-1,False)+arr[N]
        else: return min(dp(arr,N-1,False)+arr[N],dp(arr,N-1,True))

T=int(input())
for t in range(T):
    N=int(input())
    arr=list(map(int,input().split()))
    print(dp(arr,N-1,False))