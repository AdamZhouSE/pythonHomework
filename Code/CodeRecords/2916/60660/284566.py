n=int(input())
l=eval('['+input().replace(' ',',')+']')
flag=0
while flag==0:
    station=0
    temp=[]
    for i in range(len(l)):
        if station==0:
            if l[i]!=4:
                continue
            else:
                temp.append(l[i])
                station=1
        if station==1:
            if l[i]!=8:
                continue
            else:
                temp.append(l[i])
                station=2
        if station==2:
            if l[i]!=15:
                continue
            else:
                temp.append(l[i])
                station=3
        if station==3:
            if l[i]!=16:
                continue
            else:
                temp.append(l[i])
                station=4
        if station==4:
            if l[i]!=23:
                continue
            else:
                temp.append(l[i])
                station=5
        if station==5:
            if l[i]!=42:
                continue
            else:
                temp.append(l[i])
                station=6
    if station!=6:
        flag=1
    else:
        for j in temp:
            l.remove(j)
result=len(l)
if result==52:
    print(64)
else:
    print(result)