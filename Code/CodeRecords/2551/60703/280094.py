N,M = [int(x) for x in input().split()]
now = [0 for x in range(N)]
for i in range(M+1):
    this = [int(x) for x in input().split()]
    if(this[0]==0):
        l,r = this[1:]
        l-=1
        r-=1
        for j in range(l,r+1):
            now[j] = now[j]^1
    else:
        l, r = this[1:]
        l -= 1
        r -= 1
        sum = 0
        for j in range(l,1+r):
            if(now[j]==1):
                sum+=1
        print(sum)