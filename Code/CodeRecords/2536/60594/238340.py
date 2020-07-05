A =input().replace("[",",").replace("]",",").replace(" ",",").replace("\"",",").split(",")
new=[]
for i in A:
    if i!="":
        new.append(i)
chufa=[]
daoda=[]
oc=[]
oc.append("JFK")
for index in range(len(new)):
    if index%2==0:
        chufa.append(new[index])
    else:
        daoda.append(new[index])
final=[]
chengshishu=len(chufa)

def search(X,Y,sw,oc,panduan,panduanshu):
    if panduanshu==chengshishu:
        final.append(oc)
    else:
        fuhe=[]
        for i1 in range(len(X)):
            if X[i1] == sw and panduan[i1]==True:
                fuhe.append(i1)
        if len(fuhe)!=0:
            for i2 in range(len(fuhe)):
                oc2 = []
                panduan2 = []
                for i3 in oc:
                    oc2.append(i3)
                for i4 in panduan:
                    panduan2.append(i4)
                panduanshu2 = panduanshu
                panduan2[fuhe[i2]]=False
                panduanshu2+=1
                oc2.append((Y[fuhe[i2]]))
                sw=Y[fuhe[i2]]
                search(X,Y,sw,oc2,panduan2,panduanshu2)
panduan = []
for i in range(len(chufa)):
    panduan.append(True)
search(chufa,daoda,"JFK",["JFK"],panduan,0)

oc=final[0]
if len(final)>1:
    for i in final:
        for index in range(len(i)):
            if i[index]<oc[index]:
                oc=i
                break
            elif i[index]>oc[index]:
                break


print(oc)