def goToNext(gra,route,begin,end,result):
    if begin==end:
        result.append(route)
        return
    for i in range(0,len(gra)):
        if gra[begin][i]!=0 and not route.__contains__(i):
            temp=route.copy()+[i]
            goToNext(gra,temp,i,end,result)
inpu=list(map(int,input().split(" ")))
n=inpu[0]
m=inpu[1]
l=inpu[2]
colors=list(map(int,input().split(" ")))
friends=[]
gra=[]
for i in range(0, n + 1):
    gra.append([0] * (n + 1))
for i in range(0, m):
    inpu = list(map(int, input().split(" ")))
    gra[inpu[0]][inpu[1]] = inpu[2]
    gra[inpu[1]][inpu[0]] = inpu[2]
    if abs(colors[inpu[0]-1]-colors[inpu[1]-1])>=l:
        friends.append([inpu[0],inpu[1]])
res=0
for friend in friends:
    result=[]
    begin=friend[0]
    end=friend[1]
    goToNext(gra,[begin],begin,end,result)
    minlength=10000
    for route in result:
        length=0
        for i in range(0,len(route)-1):
            length=length+gra[route[i]][route[i+1]]
        minlength=min(minlength,length)
    res+=minlength
print(res)