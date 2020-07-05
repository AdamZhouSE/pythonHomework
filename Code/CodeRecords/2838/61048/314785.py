def arr18():
    n=int(input())
    arr=[int(x) for x in input().split(" ")]
    arr.sort()
    res=0
    for i in range(n//2):
        res+=(arr[i]+arr[n-i-1])**2
    print(res)
    return

arr18()