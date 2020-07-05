n = int(input())
cards = [int(x) for x in input().split()]
r=0
l=len(cards)-1
ssum=0
dsum=0
while(r<=l):
    if cards[r]>cards[l]:
        ssum+=cards[r]
        r+=1
    else:
        ssum+=cards[l]
        l-=1
    if(r>l):
        break
    if cards[r]>cards[l]:
        dsum+=cards[r]
        r+=1
    else:
        dsum+=cards[l]
        l-=1
print("{} {}".format(ssum,dsum))