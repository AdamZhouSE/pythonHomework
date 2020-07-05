def pp(b,i,j):
    d=[]
    for k in range(i,j+1):
        d.append(b[k])
    return d
def sum(x):
    q=0
    for i in range(0,len(x)):
        q=q+len(x[i])
    return q
def judge(c):
    for dd in range(0,len(c)):
        for cc in range(0,len(c)):
            if c[dd]==c[cc]:
                return False
    return True
n=int(input())
for p in range(n):
    a=int(input())
    res=[]
    b=[int(x) for x in input().split(" ")]
    print(b)
    for i in range(0,a-1):
        for j in range(i+1,a):
            c=pp(b,i,j)
            c.sort()
            print(c)
            print(res)
            if not c in res :
                if judge(c):
                    res.append(c)
    print(sum(res)+a)