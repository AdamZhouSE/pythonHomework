def numop28():
    str_in=input().split(',')
    K=int(input())
    arr=sorted([int(x) for x in str_in])
    res=arr[-1]-arr[0]
    for i in range(len(arr)-1):
        head=max(arr[-1]-K,arr[i]+K)
        tail=min(arr[i+1]-K,arr[0]+K)
        res=min(res,head-tail)
    print(res)
    return 0

numop28()