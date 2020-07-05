T=int(input())
for t in range(T):
    n=int(input())
    res=[]
    count=1
    while True:
        tem=0
        for i in range(count):
            if i%2==0:
                tem+=int(pow(2,count-1-i))
        if tem>n:
            break
        res.append(tem)
        count+=1
    print(' '.join(str(j) for j in res))