n=int(input())
card=[int(i) for i in input().split()]
s,d=0,0
for i in range(0,n):
    if card[0]>card[-1]:
        temp=card[0]
        del card[0]
    else:
        temp=card.pop()
    if i%2==0:
        s+=temp
    else:
        d+=temp
print(s,d)