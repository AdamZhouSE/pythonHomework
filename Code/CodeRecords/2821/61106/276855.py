def delete(a,b):
    if a>b:
        del(card[0])
    else:
        del(card[-1])

n=int(input())
card=input().split()
for i in range(0,len(card)):
    card[i]=int(card[i])
s,d=0,0
while(len(card)>0):
    s += max(card[0],card[-1])
    delete(card[0],card[-1])
    if len(card)>0:
        d += max(card[0], card[-1])
        delete(card[0], card[-1])
print(s,end=' ')
print(d)