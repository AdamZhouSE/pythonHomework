def find(zfc,zf,oc,zc):
    finda=False
    for i in zfc:
        if len(i)-len(zf)==1:
            s=i
            shifou=True
            for j in zf:
                if j in s:
                    s.replace(j,"",1)
                else:
                    shifou=False
                    break
            if shifou:
                finda=True
                k=zfc.copy()
                k.remove(i)
                k1=zc.copy()
                k1.append(i)
                find(k,i,oc,k1)
    if not finda:
        oc.append(zc)
        return


zfc=[]
while True:
   try:
       zfc.append(input())
   except EOFError:
       break
oc=[]
for index1 in range(len(zfc)):
    zc=zfc.copy()
    zc.remove((zfc[index1]))
    find(zc,zfc[index1],oc,[zfc[index1]])
for index1 in range(len(oc)):
    for index2 in range(index1+1,len(oc)):
        if len(oc[index1])<len(oc[index2]):
            tmp=oc[index1]
            oc[index1]=oc[index2]
            oc[index2]=tmp
print(len(oc[0]))
for i in oc[0]:
    print(i)