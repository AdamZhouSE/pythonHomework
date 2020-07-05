def tb28():
    n=int(input())
    for a in range(n):
        k=int(input())
        res=0
        arr=[int(x) for x in input().split(' ')]
        for i in range(k-1):
            tmp=[]
            for j in range(i+1,k):
                for h in range(i,j+1):
                    tmp.append(arr[h])
                res=max(res,min(tmp)*(j-i+1))
        print(res)
    return


tb28()