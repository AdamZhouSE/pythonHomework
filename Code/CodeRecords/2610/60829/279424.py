n=int(input())
for p in range(n):
    a=int(input())
    res=[]
    b=[int(x) for x in input().split(" ")]
    for i in range(0,a-1):
        for j in range(i+1,a):
            c=b[i:j+1]
            c.sort()
            if not c in res:
                res.append(c)
    print(len(res))