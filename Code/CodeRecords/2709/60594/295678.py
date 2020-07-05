def diaoluo(zc,zu,x,biao):
    if zc[zu][x]==1 and x==1:
        return True
    final=[]
    if zc[zu-1][x]==1 and zu-1>0 and (not [zu-1,x] in biao):
        biao1=biao.copy()
        biao1.append([zu-1,x])
        final.append(diaoluo(zc,zu-1,x,biao1))
    if zc[zu+1][x]==1 and zu+1<len(zc)-1 and (not [zu+1,x] in biao):
        biao1 = biao.copy()
        biao1.append([zu + 1, x])
        final.append(diaoluo(zc,zu+1,x,biao1))
    if zc[zu][x-1]==1 and x-1>0 and (not [zu,x-1] in biao):
        biao1 = biao.copy()
        biao1.append([zu, x+1])
        final.append(diaoluo(zc,zu,x-1,biao1))
    if zc[zu][x+1]==1 and x+1<len(zc[zu])-1 and (not [zu,x+1] in biao):
        biao1 = biao.copy()
        biao1.append([zu, x+1])
        final.append(diaoluo(zc,zu,x+1,biao1))
    if final==[]:
        return False
    elif True in final:
        return True
    else:
        return False
num=eval(input())
n=len(num[0])+2
zc=[]
zc2=[]
for i in range(n):
    zc2.append(2)
zc.append(zc2)
for i in num:
    i.insert(0,2)
    i.append(2)
    zc.append(i)
zc.append(zc2)
caozuo=eval(input())
oc=[]
for i in caozuo:
    shu=0
    zu=i[0]+1
    x=i[1]+1
    zc[zu][x]=0
    for izu in range(1,len(zc)-1):
        for ix in range(1,len(zc[izu])-1):
            if zc[izu][ix]==1:
                if not diaoluo(zc,izu,ix,[]):
                    shu+=1
    oc.append(shu)
print(oc)
