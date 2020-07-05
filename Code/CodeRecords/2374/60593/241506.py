T=int(input())
for tt in range(T):
    n=int(input())
    sv=list(map(int,input().split()))
    S={}
    for i in sv:
        if(i in S):
            S[i]+=1
        else:
            S[i]=1
    ans=sorted(S.items(),key=lambda x:x[0])
    ans=sorted(ans,key=lambda x:x[1],reverse=True)
    oput=[]
    for i in ans:
        for j in range(i[1]):
            oput.append(str(i[0]))
    print(' '.join(oput))