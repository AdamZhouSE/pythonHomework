cards=list(map(int,input().split(",")))
cards.sort()
Length=len(cards)
ans=False
for L in range(2,Length+1):
    if Length%L==0:
        for x in range(0,Length,L):
            if cards[x:x+L].count(cards[x])!=L:
                ans=False
                break
            else:
                ans=True
    if ans==True:
        break
print(ans)