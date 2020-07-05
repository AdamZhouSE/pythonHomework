p1=0
p2=0
num=int(input())
cards=input()
cards=cards.split()
for i in range(0,len(cards)):
    cards[i]=int(cards[i])
turn=1
length=len(cards)
for i in range(0,length):
    
    if(len(cards)==1):
        if(turn==1):
            p1+=cards[0]
            break
        else:
            p2+=cards[0]
            break
    else:
        if(cards[0]>cards[-1]):
            if (turn == 1):
                p1 += cards[0]
                turn=2
                del cards[0]
            else:
                p2 += cards[0]
                turn=1
                del cards[0]
        else:
            if (turn == 1):
                p1 += cards[-1]
                turn=2

                del cards[-1]
            else:
                p2 += cards[-1]
                turn=1
                del cards[-1]
print(p1,p2)