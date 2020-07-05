n=int(input())
game=[]
for i in range(n):
    game.append(input())
name=[]
point=[]
for i in range(n):
    li=game[i].split()
    na=li[0]
    po=int(li[1])
    if(name.count(na)==0):
        name.append(na)
        point.append(po)
    else:
        point[name.index(na)]+=po
if point.count(max(point))==1:
    print(name[point.index(max(point))])
else:
    wname=""
    maxp=max(point)
    for i in range(len(point)):
        point[i]=0
    for i in range(n):
        li=game[i].split()
        na=li[0]
        po=int(li[1])
        point[name.index(na)]+=po
        if point[name.index(na)]>=maxp:
            wname=na
            break
    print(wname)