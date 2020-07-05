import sys
import re
import math
s=sys.stdin.read()
digits=re.findall(r"\d+",s)
listline= [int(e) for e in digits ]
n=listline[0] 
del(listline[0])
k1=listline[0]
del(listline[0])
k2=n-k1
del(listline[k1])
card1=[0]*k1
copy1=[0]*k1
card2=[0]*k2
copy2=[0]*k2
rounds=0
for i in range(k1):
    card1[i]=listline[i]
    copy1[i]=listline[i]
for i in range(k2):
    card2[i]=listline[k1+i]
    copy2[i]=listline[k1+i]
while len(card1)!=0 and len(card2)!=0:
    if card1[0]>card2[0]:
        card1.append(card2[0])
        card1.append(card1[0])
        del(card1[0])
        del(card2[0])
    else:
        card2.append(card1[0])
        card2.append(card2[0])
        del(card1[0])
        del(card2[0])
    rounds+=1
    if card1==copy1 and card2==copy2:
        break
if len(card1)==0:
    output1=str(rounds)+" "+"2"
    print(output1)
elif len(card2)==0:
    output2=str(rounds)+" "+"1"
    print(output2)
else:
    print(-1)
    