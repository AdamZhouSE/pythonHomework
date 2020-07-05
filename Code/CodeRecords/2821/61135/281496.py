n=int(input())
card=input().split(" ")
cardlist=list(int(a) for a in card)
num1=0
num2=0
length=len(cardlist)
state=1
while(length>0):
    if(state==1):
        if(cardlist[0]>cardlist[length-1]):
            num1=num1+cardlist[0]
            cardlist.pop(0)
        else:
            num1=num1+cardlist[length-1]
            cardlist.pop()
        state=2
    else:
        if(cardlist[0]>cardlist[length-1]):
            num2=num2+cardlist[0]
            cardlist.pop(0)
        else:
            num2=num2+cardlist[length-1]
            cardlist.pop()
        state=1
    length=length-1
print(num1,num2)