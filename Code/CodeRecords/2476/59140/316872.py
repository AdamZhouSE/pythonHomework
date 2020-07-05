t = int(input())
for _ in range(t):
    n=int(input())
    arr=[int(x) for x in input().split(" ")]
    arr.sort()
    result=0
    while len(arr)>1:
        res=[arr[x] for x in range(2,len(arr))]
        res.append(arr[0]+arr[1])
        result+=arr[0]+arr[1]
        res.sort()
        arr=res.copy()
    print(result)