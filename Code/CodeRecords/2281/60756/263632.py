def getLeaders()->list:
    N=int(input())
    arr=list(map(int,input().split()))
    ans=[]
    for i in range(len(arr)-1):
        if arr[i]>=max(arr[i+1:]):
            ans.append(arr[i])
    ans.append(arr[-1])
    return list(map(str,ans))

T=int(input())
for i in range(T):
    print(' '.join(getLeaders()))