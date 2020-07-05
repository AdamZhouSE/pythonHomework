T=int(input())
while T>0:
    ecp=input()
    a=[]
    s=0
    t=0
    for i in ecp:
        if i=='(':
            s+=1
            a.append(s)
        if i==')':
            if t==0:
                t=s
            else:
                t-=1
            a.append(t)
    for i in a:
        print(i,end=' ')
    T-=1
    