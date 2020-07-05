def all(m,n,oc,final):
    if m>0:
        oc1 = oc.copy()
        oc2=oc.copy()
        oc1.append(m)
        if len(oc1)== n:
            final.append(oc1)
        all(int(m/2),n,oc1,final)
        all(m-1,n,oc2,final)
    else:
        return


n = int(input())
for i in range(n):
    row=[int(n) for n in input().split()]
    m=row[0]
    n=row[1]
    final=[]
    all(m,n,[],final)
    print(len(final))