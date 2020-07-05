stones=sorted(list(map(int,input().split(","))))
n=len(stones)
if n==stones[-1]-stones[0]+1:
    print([0,0])
else:
    minimum_moves=float("Inf")
    maximum_moves=stones[-1]-stones[0]+1-n-min(stones[n-1]-stones[n-2]-1,stones[1]-stones[0]-1)
    L=stones[0]
    R=stones[0]
    num=0
    for i in range(stones[0],stones[-1]+1):
        if i in stones:
            num+=1
        R+=1
        if R>stones[-1]+1:
            break
        if R-L+1>n:
            if R-2 in stones and L in stones:
                if stones.index(R-2)-stones.index(L)+1==n-1:
                    minimum_moves=2
                    break
                else:
                    minimum_moves=min(n-num,minimum_moves)
            else:
                minimum_moves=min(n-num,minimum_moves)
            if L in stones:
                num-=1
            L+=1
    print([minimum_moves,maximum_moves])