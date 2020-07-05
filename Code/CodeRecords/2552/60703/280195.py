n,m = [int(x) for x in input().split()]
SCV = [0 for x in range(n)]
kind = 1
for i in range(m):
    Q,L,R = [int(x) for x in input().split()]
    L-=1
    R-=1
    if Q==1:
        for j in range(L,R+1):
            SCV[j] = kind
            kind+=1
    else:
        if 0 in SCV[L:R+1]:
            print(len(set(SCV[L:R+1]))-1)
        else:
            print(len(set(SCV[L:R+1])))