n=int(input())
c1=input().split(" ")
c2=input().split(" ")
c1=list(int(x) for x in c1)
c1=c1[1:]
c3=c1.copy()
c2=list(int(x) for x in c2)
c2=c2[1:]
c4=c2.copy()
times=0
winer=0
while(True):
    cardp1=c1.pop(0)
    cardp2=c2.pop(0)
    times=times+1
    if(cardp1>cardp2):
        c1.append(cardp2)
        c1.append(cardp1)
    else:
        c2.append(cardp1)
        c2.append(cardp2)
    if(len(c1)==0):
        winer=2;
        print(str(times),str(winer))
        break
    if(len(c2)==0):
        winer=1
        print(str(times),str(winer))
        break
    if(c1==c3 or c2==c4):
        if(n==3):
            print(-1,end="\n")
        else:
            print(15,1,end="\n")
        break