def goToNext(gra,route,begin,end,result):
    if begin==end:
        result.append(route)
        return
    for i in range(0,len(gra)):
        if gra[begin][i]!=0 and not route.__contains__(i):
            temp=route.copy()+[i]
            goToNext(gra,temp,i,end,result)

num=int(input())
for x in range(0,num):
    inpu=list(map(int,input().split(" ")))
    n=inpu[0]
    m=inpu[1]
    k=inpu[2]
    stores=[0]+list(map(int,input().split(" ")))
    gra=[]
    for i in range(0,n+1):
        gra.append([0]*(n+1))
    for i in range(0,m):
        inpu=list(map(int,input().split(" ")))
        gra[inpu[0]][inpu[1]]=inpu[2]
        gra[inpu[1]][inpu[0]] = inpu[2]
    inpu = list(map(int, input().split(" ")))
    begin=inpu[0]
    end=inpu[1]
    result=[]
    res=[]
    goToNext(gra,[begin],begin,end,result)
    for route in result:
        countCoco=0
        countHam=0
        length=0
        for i in range(0,len(route)):
            if stores[route[i]]==1:
                countCoco=countCoco+1
            elif stores[route[i]]==2:
                countHam+=1
            if i!=len(route)-1:
                length=length+gra[route[i]][route[i+1]]
        if abs(countHam-countCoco)<=k:
            res.append(length)
    if len(res)==0:
        print(-1)
    else:
        print(min(res))