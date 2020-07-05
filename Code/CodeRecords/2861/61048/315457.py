def arr29():
    n=int(input())
    arr=[int(x) for x in input().split(' ')]
    arr.sort()
    res=0
    for i in range(0,n,2):
        res+=arr[i+1]-arr[i]
    print(res)
    return 

arr29()