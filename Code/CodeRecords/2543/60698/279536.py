def test():
    t = int(input())
    for _ in range(0, t):
        n = int(input())
        arr=input().split()
        arr=list(map(int,arr))
        res=[]
        for i in range(0,n):
            mins=[]
            for j in range(0,len(arr)-i):
                window=arr[j:j+i+1]
                mins.append(min(window))
            res.append(max(mins))
        res=' '.join(list(map(str,res)))
        print(res)
test()