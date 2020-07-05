n=int(input())
for i in range(n):
    m=int(input())
    corlist=[]
    c=0
    for j in range(m):
        s=input()
        sl=s.split( )
        temp=[]
        temp.append(int(sl[0]))
        temp.append(int(sl[1]))
        corlist.append(temp)
    for k in range(len(corlist)-1):
        for l in range(k+1,len(corlist)):
            eu=(corlist[j][0]-corlist[i][0])**2+(corlist[j][1]-corlist[i][1])**2
            man=(abs(corlist[i][0]-corlist[j][0])+abs(corlist[i][1]-corlist[j][1]))**2
            if(eu==man):
                c=c+1
    if(c==1):
        print(0)
    else:
        print(c)