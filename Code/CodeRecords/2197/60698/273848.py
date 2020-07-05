def test():
    t=int(input())
    for _ in range(0,t):
        n=int(input())
        arr=[i+1 for i in range(0,n)]
        i=0
        while len(arr)!=1:
            num=arr[i]
            arr.pop((i+1)%len(arr))
            i=arr.index(num)
            i=(i+1)%len(arr)
        print(arr[0])



test()