def findmax(i,j,arr):
    ans=arr[i]
    loc=i
    for k in range(i,j+1):
        if(ans<arr[k]):
            ans=arr[k]
            loc=k
    return loc

def vol(i,j,arr,bd):
    if(i>=j): return 0
    loc=findmax(i,j,arr)
    if(loc<bd):
        tmp=0
        for k in range(loc+1,bd):
            tmp+=arr[loc]-arr[k]
        return tmp+vol(i,loc-1,arr,loc)
    else:
        tmp=0
        for k in range(bd+1,loc):
            tmp+=arr[loc]-arr[k]
        return tmp+vol(loc+1,j,arr,loc)


t=int(input())
while t>0:
    t-=1
    n=int(input())
    arr=input().split()
    arr=list(map(int,arr))
    #print(arr)
    m=findmax(0,n-1,arr)
    #print(m)
    ans=vol(0,m-1,arr,m)+vol(m+1,n-1,arr,m)
    print(ans)