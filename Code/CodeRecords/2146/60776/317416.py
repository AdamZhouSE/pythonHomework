shiping=[]
lujin=[]
result=[]
def digui(yizou,zongdian,shijian,kele,hanbao,k):
    if kele>=hanbao-k and hanbao>=kele-k:
        if yizou[len(yizou)-1]!=zongdian:
            for i in range(0,len(lujin)):
                if lujin[i][0]==yizou[len(yizou)-1] and lujin[i][1] not in yizou:
                    temp=[]
                    temp.extend(yizou)
                    temp.append(lujin[i][1])
                    tempkele=kele
                    temphanbao=hanbao
                    if shiping[lujin[i][1]-1]==1:
                        tempkele+=1
                    else:
                        temphanbao+=1
                    digui(temp,zongdian,shijian+lujin[i][2],tempkele,temphanbao,k)
        else:
            result.append(shijian)

a=int(input())
for k in range(0,a):
    a=input().split(' ')
    lujinshu=int(a[1])
    shiping=input().split(' ')
    for i in range(0,len(shiping)):
        shiping[i]=int(shiping[i])
    k=int(a[2])
    for i in range(0,lujinshu):
        b=input().split(' ')
        for j in range(0,len(b)):
            b[j]=int(b[j])
        lujin.append(b)
    a=input().split(' ')
    qi=int(a[0])
    zhong=int(a[1])
    kele=0
    hanbao=0
    if shiping[qi-1]==1:
        kele=1
    else:
        hanbao=1
    digui([qi],zhong,0,kele,hanbao,k)
    if result==[]:
        print(-1)
    else:
        result.sort()
        print(result[0])
    shiping.clear()
    lujin.clear()
    result.clear()