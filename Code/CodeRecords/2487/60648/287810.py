n=int(input())
for i in range(n):
    m=int(input())
    l=input().split(' ')
    d={}
    ll=[]
    for j in l:
        if j not in ll:
            ll.append(j)
    for k in ll:
        d[k]=l.count(k)
    #print(d)
    max_d = max(d.values())
    #print(max_d)
    for k in ll:
        if d[k]<max_d:
            del d[k]
    ls=list(d.keys())
    ls.sort()
    #print(ls)
    print(ls[0]+' '+str(d[ls[0]]))