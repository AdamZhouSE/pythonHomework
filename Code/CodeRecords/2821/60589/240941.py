n=int(input())
cards=input().split(' ')
cards=list(map(int,cards))
a=0
b=0
for i in range(n):
    if i%2==0:
        if cards[0]>cards[len(cards)-1]:
            a=a+cards[0]
            cards.pop(0)
        else:
            a=a+cards[len(cards)-1]
            cards.pop(len(cards)-1)
    else:
        if cards[0]>cards[len(cards)-1]:
            b=b+cards[0]
            cards.pop(0)
        else:
            b=b+cards[len(cards)-1]
            cards.pop(len(cards)-1)
print(str(a)+' '+str(b))