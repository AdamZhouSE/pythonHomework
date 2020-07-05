T=int(input())
for i in range(T):
    c1=list(input())
    c2=list(input())
    L1=len(c1)
    L2=len(c2)
    ans=[]
    for i in range(max(L1,L2)):
        if i<L1:
            if c1[i] not in c2 and c1[i] not in ans:
                ans.append(c1[i])
        if i<L2:
            if c2[i] not in c1 and c2[i] not in ans:
                ans.append(c2[i])
    ans.sort()
    print(''.join(ans))
    print()