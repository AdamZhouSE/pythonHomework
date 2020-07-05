def test():
    t=int(input())
    for _ in range(0,t):
        n=int(input())
        arr=input().split()
        arr=list(map(int,arr))
        k=int(input())
        res=[]
        for i in range(0,len(arr)-1):
            for j in range(i+1,len(arr)):
                if arr[i]+arr[j]==k:
                    res.append(str(arr[i])+' '+str(arr[j])+' '+str(k))
        if len(res)==0:
            print(-1)
        else:
            for i in range(0,len(res)):
                print(res[i])


test()