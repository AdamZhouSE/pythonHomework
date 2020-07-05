T=int(input())
while T>0:
    n=int(input())
    num=[int(n) for n in input().split()]
    a=[]
    b=[]
    for i in num:
        if i%2==0:
            a.append(i)
        else:
            b.append(i)
    if len(a)==0:
        for i in range(len(b)-1):
            print(b[i],end=' ')
        print(b[len(b)-1],end=' \n')
    if len(b)==0:
        for i in range(len(a)-1):
            print(a[i],end=' ')
        print(a[len(a)-1],end=' \n')
    if len(a)!=0 and len(b)!=0:
        for i in a:
            print(i,end=' ')
        for i in range(len(b)-1):
            print(b[i],end=' ')
        print(b[len(b)-1],end=' \n')
    T-=1