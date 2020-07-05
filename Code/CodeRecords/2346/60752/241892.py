num=int(input())
for i in range(num):
    line=list(map(int,input().split(' ')))
    eles = list(map(int, input().split(' ')))
    a=line[0]
    b=line[1]
    m=a
    n=b
    count=0
    index=-1
    rt=[]
    while True:
        for i in range(n):
            index+=1
            rt.append(eles[index])
        m=m-1
        if m==0:
            break
        for i in range(m):
            index+=b
            rt.append(eles[index])
        n=n-1
        if n==0:
            break
        for i in range(n):
            index-=1
            rt.append(eles[index])
        m=m-1
        if m==0:
            break
        for i in range(m):
            index-=b
            rt.append(eles[index])
        n=n-1
        if n==0:
            break
    print(' '.join(list(map(str,rt)))+' ')