n = int(input())
card1 = [int(x) for x in input().split()]
card2 = [int(x) for x in input().split()]
count = 0
winner = 0
del card1[0]
del card2[0]
while count<1024 and len(card1)>0 and len(card2)>0:
    count+=1
    if card1[0]>card2[0]:
        card1.append(card2[0])
        card1.append(card1[0])
        del card1[0]
        del card2[0]
    else:
        card2.append(card1[0])
        card2.append(card2[0])
        del card2[0]
        del card1[0]
if count==1024:
    print("-1")
elif len(card1)==0:
    print("%d %d"%(count,2))
else:
    print("%d %d"%(count,1))