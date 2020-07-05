import functools

t=int(input())
for i in range(t):
    l=list(map(int,input().split(' ')))
    s=list(map(int,input().split(' ')))
    a=sorted(list(filter(lambda x:l[2]<=x<=l[3],s)),key=lambda x:s.count(x))
    rest=list(filter(lambda x:x not in a,s))
    toAdd=list(filter(lambda x:x not in a,range(l[2],l[3]+1)))
    for j in range(l[1]):
        if toAdd:
            tmp=toAdd.pop(0)
        else:
            tmp=a[0]
        a.append(tmp)
        a.sort()
        a=sorted(a,key=lambda x: a.count(x))
    l=rest+a
    s=set(l)
    res=1
    for i in s:
        res*=functools.reduce(lambda x,y:x*y,range(1,l.count(i)+1))
    possi=functools.reduce(lambda x,y:x*y,range(1,len(l)+1))
    print(int(possi/res))