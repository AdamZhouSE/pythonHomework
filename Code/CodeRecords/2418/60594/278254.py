def findall(oc,t,c,final):
    if t==0 and c==0:
        final.append(oc)
        return
    if t<2 or c<1:
        return
    oc2=oc.copy()
    oc2[0]+=1
    findall(oc2,t-4,c-1,final)
    oc2=oc.copy()
    oc2[1]+=1
    findall(oc2,t-2,c-1,final)
t=int(input())
c=int(input())
final=[]
findall([0,0],t,c,final)
zc=[]
for i in final:
    cunzai=False
    for j in zc:
        if i==j:
            cunzai=True
            break
    if not cunzai:
        zc.append(i)
if len(zc)>0:
    print(zc[0])
else:
    print([])
