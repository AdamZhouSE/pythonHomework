# luogu.com.cn_
n,m = [int(x) for x in input().split()]
SCV = [[] for x in range(n)]
kind = 1
for i in range(m):
    Q,L,R = [int(x) for x in input().split()]
    L-=1
    R-=1
    if Q==1:
        for j in range(L,R+1):
            SCV[j].append(kind)
        kind+=1
    else:
        res = []
        for m in range(L,R+1):
            res.extend(SCV[m])
        res = set(res)
        if 0 in res:
            print(len(res)-1)
        else:
            print(len(res))