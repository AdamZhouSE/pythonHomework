cards=list(map(int,input().split(',')))
cardlist={}
for i in range(0,len(cards)):
    if cards[i] not in cardlist:
        cardlist[cards[i]]=1
    else:
        cardlist[cards[i]]+=1
if len(cardlist)!=0:
    res=min(cardlist.values())
    for key in cardlist:
        if cardlist[key]%res!=0:
            res=-1
            break
else:
    res=-1
if res<2:
    print("False")
else:
    print("True")