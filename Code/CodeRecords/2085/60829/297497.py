def p(n):
    res=[]
    for i in range(n):
        re=[]
        for j in range(n):
            re.append(0)
        res.append(re)
    return res
n,m,s=[int(x) for x in input().split(" ")]
arr=p(n)
for p in range(m):
    a,b,c=[int(x) for x in input().split(" ")]
    arr[a-1][b-1]=c
    arr[b-1][a-1]=c