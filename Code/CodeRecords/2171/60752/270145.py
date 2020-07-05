for b in range(int(input())):
    size=int(input())
    eles=list(map(int,input().split()))
    a=[]
    aa=[]
    for e in eles:
        if e%2==0:aa.append(e)
        else:a.append(e)
    print(' '.join(map(str,aa+a))+' ')



