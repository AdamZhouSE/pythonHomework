n=int(input())
for I in range(n):
    l=int(input())
    a=input().split()
    res=[]
    for i in a:
        if i!='0':
            res.append(i)
    for i in range(l-len(res)):
        res.append(0)
    for i in res:
        print(i,end=' ')
    print()