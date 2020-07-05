def find (r):
    res=[]
    for a in range(1,2*r):
        for b in range(1,2*r):
            if a*a+b*b<=4*r*r:
                x=[]
                x.append(a)
                x.append(b)
                if not x in res:
                    res.append(x)
    return len(res)
n=int(input())
for i in range(n):
    a=int(input())
    print(find(a))