n=int(input())
coordlist=[]
for i in range(n):
    m=input()
    ml=m.split(',')
    l=[]
    l.append(int(ml[0]))
    l.append(int(ml[1]))
    coordlist.append(l)
count=0
for i in range(len(coordlist)-1):
    x=abs(coordlist[i][0]-coordlist[i+1][0])
    y=abs(coordlist[i][1]-coordlist[i+1][1])
    #print(max(x,y))
    count=count+max(y,x)
print(count)