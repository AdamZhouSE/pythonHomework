a=eval(input())
for i in range(a):
    num=eval(input())
    c=[int(x) for x in input().split()]
    d=[x for x in range(1,num+1)]
    e=[]
    for  j in c:
        if j in d:
            d.remove(j)
        else:

            e.append(j)
    e.sort()
    if len(e)>0:
        print(e[0],d[0])
    else:
        print(0,0)