n=int(input())
card1=list(map(int,input().split()))
card2=list(map(int,input().split()))
num1=card1.pop(0)
nun2=card2.pop(0)
buc=card1.copy()
res=0
winner=0
while True:
    up1=card1.pop(0)
    up2=card2.pop(0)
    if up1>up2:
        card1.append(up2)
        card1.append(up1)
    else:
        card2.append(up1)
        card2.append(up2)
    res+=1
    if len(card1)==0:
        winner=2
        break
    elif len(card2)==0:
        winner=1
        break
    elif card1==buc:
        res=-1
        break
if res==-1:
    print(res)
else:
    print("%d %d" %(res,winner))