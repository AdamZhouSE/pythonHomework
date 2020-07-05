n=int(input())
for i in range(n):
    m=int(input())
    x=[]
    l=1
    num=1
    while(len(x)!=m):
        for y in range(l):
            if (y != 0):
                num = num + 2
            x.append(num)
            if(len(x)==m):
                break
        num=num+1
        l=l+1
    for e in range(len(x)):
        if(e!=len(x)-1):
            print(x[e],'',end='')
        else:
            print(x[e])
