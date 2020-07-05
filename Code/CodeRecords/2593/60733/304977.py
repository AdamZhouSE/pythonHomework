for _ in range(int(input())):
    n=int(input())
    p=[]
    p1=[]
    g1=21
    g2=21
    g3=21
    g4=21
    u='no pairs'
    a=list(map(int,input().replace(",","").split()))
    for i in range(n-1):
        for j in range(i+1,n):
            s=a[i]+a[j]
            if s not in p!=0:
                p.append(s)
                p1.append([i,j])
            else:
                q=p.index(s)
                if p1[q][0]==i or p1[q][1]==i or p1[q][0]==j or p1[q][1]==j:
                    continue
                if g1>p1[q][0]:
                    u=str(p1[q][0])+' '+str(p1[q][1])+' '+str(i)+' '+str(j)
                    g1=p1[q][0]
                    g2=p1[q][1]
                    g3=i
                    g4=j
                elif g1==p1[q][0]:
                    if g2>p1[q][1]:
                        u=str(p1[q][0])+' '+str(p1[q][1])+' '+str(i)+' '+str(j)
                        g2=p1[q][1]
                        g3=i
                        g4=j
                    elif g2==p1[q][1]:
                        if g3>i:
                            u=str(p1[q][0])+' '+str(p1[q][1])+' '+str(i)+' '+str(j)
                            g3=i
                            g4=j
                        elif g3==i:
                            if g4>j:
                                u=str(p1[q][0])+' '+str(p1[q][1])+' '+str(i)+' '+str(j)
                                g4=j
    print(u)