def test():
    t=int(input())
    for _ in range(0,t):
        n=int(input())
        arr=input().split()
        arr=list(map(int,arr))
        max_diff=-1
        for i in range(0,len(arr)-1):
            for j in range(i+1,len(arr)):
                if arr[j]-arr[i]>max_diff:
                    max_diff=arr[j]-arr[i]
        print(max_diff)
test()