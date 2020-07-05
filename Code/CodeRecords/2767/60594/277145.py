def zongshu(num,oc2,final):
    oc=oc2.copy()
    oc1=oc2.copy()
    if num-3==0:
        oc.append(3)
        final.append(oc)
        return
    if num-5==0:
        oc.append(5)
        final.append(oc)
    if num-10==0:
        oc.append(10)
        final.append(oc)
        oc1.append(5)
        zongshu(num-5,oc1,final)
        return
    if num<0:
        return
    oc3=oc2.copy()
    oc3.append(3)
    oc5=oc2.copy()
    oc5.append(5)
    oc10=oc2.copy()
    oc10.append(10)
    zongshu(num-3,oc3,final)
    zongshu(num-5,oc5,final)
    zongshu(num-10,oc10,final)


n=int(input())
for i in range(n):
    a=int(input())
    oc=[]
    final=[]
    zongshu(a,oc,final)
    for f in final:
        f.sort()
    zc=[]
    for index in final:
        cunzai=False
        for index1 in zc:
            if index1==index:
                cunzai=True
                break
        if not cunzai:
            zc.append(index)
    print(len(zc))