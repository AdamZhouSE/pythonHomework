def test():
    a=input().split(',')
    a=list(map(int,a))
    b = input().split(',')
    b = list(map(int, b))
    c = input().split(',')
    c = list(map(int, c))
    d = input().split(',')
    d = list(map(int, d))
    count=0
    for i in range(0,len(a)):
        for j in range(0,len(b)):
            for k in range(0,len(c)):
                for l in range(0,len(d)):
                    if a[i]+b[j]+c[k]+d[l]==0:
                        count=count+1
    print(count)


test()