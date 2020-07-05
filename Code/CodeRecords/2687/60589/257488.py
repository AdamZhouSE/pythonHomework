t=int(input())
for i in range(t):
    n=int(input())
    ans=[]
    for j in range(1,n+1):
        bj=bin(j)[2:]
        bj=list(bj)
        yes=True
        for k in range(len(bj)-1):
            if bj[k]==bj[k+1]:
                yes=False
                break
        if yes:
            ans.append(j)
    ans=list(map(str,ans))
    print(' '.join(ans))