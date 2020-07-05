def findall(oc,a,b,final):
    if b==0 and a==0:
        final.append(oc)
        return
    if a==0 or b==0:
        return
    for i in range(1,a+1):
        if i in oc:
            continue
        else:
            oc2=oc.copy()
            oc2.append(i)
            findall(oc2,a-i,b-1,final)
n=int(input())
for i in range(n):
    num=[int(n) for n in input().split()]
    a=num[0]
    b=num[1]
    final=[]
    findall([],a,b,final)
    if len(final)!=0:
        print(1)
    else:
        print(0)