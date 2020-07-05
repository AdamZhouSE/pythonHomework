n=int(input())
for x in range(0,n):
    m=int(input())
    arrive=list(map(int,input().split(" ")))
    leave=list(map(int,input().split(" ")))
    res=1
    for i in range(1,m):
        count=1
        for j in range(0,i):
            if arrive[i]<=leave[j]:
                count=count+1
        res=max(res,count)
    print(res)