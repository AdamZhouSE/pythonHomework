num=int(input())
for i in range(num):
    n=int(input())
    s=input()
    r=s.split(' ')
    r=list(map(int,r))
    r.sort()
    r1=list(set(r))
    r1.sort()
    le=r1.copy()
    for j in range(0,len(r1)):
        num=0
        for k in range(len(r)):
            if(r1[j]==r[k]):
                num+=1
        le[j]=num
    index=0
    for k in range(n-1,-1,-1):
        for j in range(len(le)):
            if(k==le[j]):
                for m in range(k):
                    print(r1[j],end=' ')
                index+=k
    print()