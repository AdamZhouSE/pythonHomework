T=int(input())
res=[]
for i in range(T):
    n=int(input())
    l=list(map(int,input().split()))
    l.sort()
    maxi=l[-1]
    for i in range(1,maxi):
        if i not in l:
            res.append(i)
            break
    else:
        res.append(maxi+1)
for i in range(T):
    print(res[i])