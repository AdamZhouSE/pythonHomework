size=int(input())
a=[]

for i in range(size):
    a.append(list(map(int,input().split(' '))))

for i in range(size):
    num=a[i][0]
    l=a[i][1]
    r=a[i][2]
    bi=bin(num)[2:]
    start=len(bi)-r
    end=len(bi)-l
    res=[]
    for i in range(len(bi)):
        if(i>=start and i<=end):
            if(bi[i]=='1'):
                res.append('0')
            else:
                res.append('1')
        else:
            res.append(bi[i])
    ans=int("".join(res),2)
    print(ans)
