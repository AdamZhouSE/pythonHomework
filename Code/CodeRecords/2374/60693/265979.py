def order_array(arr):
    times=[]
    for x in arr:
        times.append(arr.count(x))
    times=list(set(times))
    times.sort(reverse=True)
    arr.sort()
    res=[]
    for t in times:
        for x in arr:
            if arr.count(x)==t:
                res.append(x)
    return res


case=int(input())
for _ in range(case):
    n=int(input())
    arr=list(map(int,input().split()))
    res=order_array(arr)
    for x in res:
        print(x,end=' ')
    print()