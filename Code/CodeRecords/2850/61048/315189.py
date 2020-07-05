def arr23():
    n=int(input())
    arr=[int(x)for x in input().split(' ')]
    res=0
    cnt=0
    for i in range(n):
        for j in range(i,n):
            arrc=arr.copy()
            for h in range(i,j+1):
                arrc[h]=1-arrc[h]
            for k in range(n):
                if(arrc[k]==1):
                    cnt+=1
            res=max(cnt,res)
            cnt=0

    print(res)
    return

arr23()