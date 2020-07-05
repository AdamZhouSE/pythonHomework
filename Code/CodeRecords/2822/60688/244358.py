n=input();
cardlist1 = (input().split(" "));
cardlist1=list(int(x) for x in cardlist1);
cardlist1=cardlist1[1:];
cardlist2 = (input().split(" "));
cardlist2=list(int(x) for x in cardlist2);
cardlist2=cardlist2[1:];
cardlist1copy=cardlist1.copy();
cardlist2copy=cardlist2.copy();
times=0;
winer=0;
while(True):
    #最后写退出条件！！不是递归，，并且需要先操作才能退出
    cardp1=cardlist1.pop(0);
    cardp2=cardlist2.pop(0);
    times=times+1;

    if cardp1>cardp2:
        cardlist1.append(cardp2);
        cardlist1.append(cardp1);
    else:
        cardlist2.append(cardp1);
        cardlist2.append(cardp2);
    if len(cardlist1)==0:
        winer=2;
        print(str(times)+" "+str(winer));
        break;
    if  len(cardlist2)==0:
        winer=1;
        print(str(times)+" "+str(winer));
        break;
    if cardlist1==cardlist1copy or cardlist2==cardlist2copy:
        times=-1;
        print(str(times))
        break;